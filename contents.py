import tensorflow as tf
import numpy as np
import os
import cv2
from tensorflow.keras.preprocessing import image

# Load the trained MobileNetV2 model
model_path = "E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/E-Waste_Non-Ewaste_classifier.h5"  # Update with your actual model path
model = tf.keras.models.load_model(model_path)

# Define class labels (update according to your dataset structure)
class_labels = ['e-waste', 'non-e-waste']  # Main classification

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # MobileNetV2 input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array

# Provide the image path manually
image_path = r"E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/test_images/download.jpg"  # Update this

if os.path.exists(image_path):
    img_array = preprocess_image(image_path)
    
    # Perform prediction
    predictions = model.predict(img_array)
    primary_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0]) * 100
    
    if confidence < 50:
        print(f"{os.path.basename(image_path)}: Unable to confidently classify the image.")
    else:
        primary_label = class_labels[primary_class]
        print(f"{os.path.basename(image_path)}: Detected as {primary_label} with {confidence:.2f}% confidence.")
else:
    print("Image path does not exist. Please provide a valid path.")



