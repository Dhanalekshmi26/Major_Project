import os
import json
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Define paths dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Fixed the typo
json_class_path = os.path.join(BASE_DIR, "class_labels.json")
json_recycle_path = os.path.join(BASE_DIR, "recycling_info.json")
ewaste_model_path = os.path.join(BASE_DIR, "ewaste_mobilenetv2.h5")

# Load JSON files
with open(json_class_path, "r", encoding="utf-8") as file:
    class_labels = json.load(file)

with open(json_recycle_path, "r", encoding="utf-8") as file:
    recycling_info = json.load(file)

# Load trained CNN model
ewaste_model = load_model(ewaste_model_path)

# Import optimal thresholds
from thresholds import optimal_thresholds

def load_and_preprocess_image(image_path):
    """ Load and preprocess image for model prediction """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return None
    image = cv2.resize(image, (224, 224))
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def detect_device(image_path):
    """ Detect the electronic device from image """
    image = load_and_preprocess_image(image_path)
    if image is None:
        return None

    predictions = ewaste_model.predict(image)[0]
    detected_devices = []

    for idx, score in enumerate(predictions):
        class_idx_str = str(idx)
        if class_idx_str in class_labels:
            class_name = class_labels[class_idx_str]

            # **Only allow classes that exist in optimal_thresholds**
            if class_name in optimal_thresholds:
                threshold = optimal_thresholds[class_name]
                if score >= threshold:
                    detected_devices.append((class_name, score))

    # **Check if any valid e-waste objects were detected**
    if not detected_devices:
        print("\n This is NON-E-WASTE. It cannot be recycled as e-waste.")
        return None  # Non-e-waste detected

    # **Sort detected devices by confidence**
    detected_devices.sort(key=lambda x: x[1], reverse=True)

    return detected_devices

def predict_recycling_methods(detected_devices):
    """ Fetch recycling details based on detected devices """
    for device, score in detected_devices:
        print(f"\n✅ Detected Device: {device} (Confidence: {score:.2f})")

        # Fetch recycling info
        if device in recycling_info:
            internal_components = recycling_info[device].get("internal_components", [])
            recycling_methods = recycling_info[device].get("recycling_methods", {})

            print("\n🔍 Internal Components:")
            for component in internal_components:
                print(f"- {component}: {recycling_methods.get(component, 'No recycling method available')}")
        else:
            print("⚠️ No recycling data available for this device.")

if __name__ == "__main__":  # Fixed the typo
    # Provide image path
    image_path = "E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/test_images/hhh.jpg"
    
    if os.path.exists(image_path):
        detected_devices = detect_device(image_path)
        if detected_devices:
            predict_recycling_methods(detected_devices)
    else:
        print(f"Error: The path '{image_path}' does not exist.")
