import os
import json
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_class_path = os.path.join(BASE_DIR, "class_labels.json")
json_recycle_path = os.path.join(BASE_DIR, "recycling_info.json")
ewaste_model_path = os.path.join(BASE_DIR, "ewaste_mobilenetv2.h5")  # First Model
classifier_model_path = os.path.join(BASE_DIR, "E-Waste_Non-Ewaste_classifier.h5")  # Second Model

# Load JSON files
with open(json_class_path, "r", encoding="utf-8") as file:
    class_labels = json.load(file)

with open(json_recycle_path, "r", encoding="utf-8") as file:
    recycling_info = json.load(file)

# Load trained CNN models
ewaste_model = load_model(ewaste_model_path)
classifier_model = load_model(classifier_model_path)  # Load second model

# Import optimal thresholds for the first model
from thresholds import optimal_thresholds

# List of internal components (modify if needed)
INTERNAL_COMPONENTS = ["Battery","Inductor","PCB","capacitor","cpu","diode","integrated circuit","resistor",
                       "transformer","transistor"]

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
    """ Detect the electronic device from image using first model """
    image = load_and_preprocess_image(image_path)
    if image is None:
        return None

    predictions = ewaste_model.predict(image)[0]
    detected_devices = []

    for idx, score in enumerate(predictions):
        class_idx_str = str(idx)
        if class_idx_str in class_labels:
            class_name = class_labels[class_idx_str]

            # Check if class exists in optimal_thresholds
            if class_name in optimal_thresholds:
                threshold = optimal_thresholds[class_name]
                if score >= threshold:
                    detected_devices.append((class_name, score))

    # If no detected devices or confidence is ≤ 0.6, use the second model
    if not detected_devices:
        return check_ewaste_or_not(image)

    # Sort detected devices by confidence
    detected_devices.sort(key=lambda x: x[1], reverse=True)
    return detected_devices

def check_ewaste_or_not(image):
    """ Use the second model to determine if the image is e-waste or non-e-waste """
    prediction = classifier_model.predict(image)[0]
    ewaste_score = prediction[0]  # Assuming e-waste is class 0

    if ewaste_score >= 0.6:
        print("\n Classified as E-WASTE")
        return [("This is E-WASTE", ewaste_score)]
    else:
        print("\n This is NON-E-WASTE. It cannot be recycled as e-waste.")
        return None

def predict_recycling_methods(detected_devices):
    """ Fetch recycling details based on detected devices """
    for device, score in detected_devices:
        print(f"\n Detected: {device} (Confidence: {score:.2f})")

        # Check if detected object is an internal component
        if device in INTERNAL_COMPONENTS:
            print(f" Detected {device}.")
            return  # Stop further processing if an internal component is detected

        # Fetch recycling info for external devices
        if device in recycling_info:
            internal_components = recycling_info[device].get("internal_components", [])
            recycling_methods = recycling_info[device].get("recycling_methods", {})

            print("\n Internal Components & Recycling Methods:")
            for component in internal_components:
                print(f"- {component}: {recycling_methods.get(component, 'No recycling method available')}")
        else:
            print(" No recycling data available for this device.")

if __name__ == "__main__":
    # Provide image path
    image_path = r"debug_preprocessed.jpg"
    
    if os.path.exists(image_path):
        detected_devices = detect_device(image_path)
        if detected_devices:
            predict_recycling_methods(detected_devices)
    else:
        print(f"Error: The path '{image_path}' does not exist.")