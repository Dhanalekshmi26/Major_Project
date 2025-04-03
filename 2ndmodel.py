import tensorflow as tf
import numpy as np
import cv2
import os

# Load the trained model
model_path = "E-Waste_Non-Ewaste_classifier.h5"
model = tf.keras.models.load_model(model_path)

# Function to preprocess the image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return None
    image = cv2.resize(image, (224, 224))  # Resize to match model input
    image = image.astype("float32") / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to predict whether an image is E-Waste or Non-E-Waste
def predict_image(image_path):
    image = preprocess_image(image_path)
    if image is None:
        return
    
    prediction = model.predict(image)[0][0]  # Get prediction score

    if prediction >= 0.5:
        print(f" Non-E-Waste (Score: {prediction:.2f})")
    else:
        print(f" E-Waste (Score: {prediction:.2f})")

# 📌 Provide the image path you want to check
image_path = "E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/test_images/download (17).jpg"  # Change this to the actual image path
if os.path.exists(image_path):
    predict_image(image_path)
else:
    print(f"Error: File '{image_path}' not found.")

