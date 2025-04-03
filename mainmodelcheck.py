import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

# Load the model
model_path = "E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/E-Waste_Non-Ewaste_classifier.h5"
model = tf.keras.models.load_model(model_path)

# Provide a direct image path (change this to the actual image file you want to test)
img_path = "E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/test_images/download (5).jpg"

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0  # Normalize
    return np.expand_dims(img_array, axis=0)

# Run prediction on the single image
img_array = preprocess_image(img_path)
predictions = model.predict(img_array)[0]

# Assuming it's a binary classification: 0 = Non-E-Waste, 1 = E-Waste
confidence = predictions[0]

if confidence > 0.5:
    print(f"[❌ Incorrect] The image is misclassified as E-Waste (Confidence: {confidence:.2f})")
else:
    print(f"[✅ Correct] The image is classified as Non-E-Waste (Confidence: {confidence:.2f})")




