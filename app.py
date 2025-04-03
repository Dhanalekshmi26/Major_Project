import os
import json
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename


# Initialize Flask app
app = Flask(__name__)

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set upload folder in Flask config
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
classifier_model = load_model(classifier_model_path)

# Import optimal thresholds
from thresholds import optimal_thresholds

# List of internal components
INTERNAL_COMPONENTS = ["Battery", "Inductor", "PCB", "Capacitor", "CPU", "Diode", "Integrated Circuit", "Resistor",
                       "Transformer", "Transistor"]

def load_and_preprocess_image(image_path):
    """ Load and preprocess image for model prediction """
    image = cv2.imread(image_path)
    if image is None:
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

    if ewaste_score < 0.5:
        return [("This is E-WASTE", ewaste_score)]
    else:
        return [("This is NON-E-WASTE", ewaste_score)]

def predict_recycling_methods(detected_devices):
    """ Fetch recycling details based on detected devices """
    recycling_data = []

    for device, score in detected_devices:
        if device in INTERNAL_COMPONENTS:
            return [{"device": device, "message": "Internal component detected."}]

        if device in recycling_info:
            internal_components = recycling_info[device].get("internal_components", [])
            recycling_methods = recycling_info[device].get("recycling_methods", {})

            recycling_data.append({
                "device": device,
                "confidence": f"{score:.2f}",
                "internal_components": internal_components,
                "recycling_methods": json.dumps(recycling_methods, indent=2)  # Format JSON for readability
            })
        else:
            recycling_data.append({"device": device, "message": "No recycling data available."})
    
    return recycling_data

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    filename = secure_filename(file.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(image_path)

    detected_devices = detect_device(image_path)
    if detected_devices:
        recycling_info_data = predict_recycling_methods(detected_devices)
        return jsonify({
            "image_url": url_for('static', filename='uploads/' + filename),
            "prediction": recycling_info_data
        })
    else:
        return jsonify({
            "message": "No e-waste detected or unable to classify the image.",
            "image_url": url_for('static', filename='uploads/' + filename)
        })

if __name__ == '__main__':
    app.run(debug=True)
