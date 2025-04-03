import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model('E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/E-Waste_Non-Ewaste_classifier.h5')

# Class labels (replace with your labels if needed)
e_waste_labels = {
    0: 'Hard disk drive', 1: 'Keyboard', 2: 'Microwave', 3: 'Mobile', 4: 'Mouse', 
    5: 'Player', 6: 'Printer', 7: 'Refrigerator', 8: 'Television', 9: 'Washing Machine',
    10: 'Circuit board', 11: 'Coin cell lithium battery', 12: 'Electrolytic capacitor',
    13: 'Hair dryer', 14: 'Iron core inductor', 15: 'Laptop', 16: 'Lead acid battery',
    17: 'Lithium iron battery', 18: 'PCB capacitors', 19: 'Remote', 
    20: 'Silver oxide battery', 21: 'Speaker', 22: 'Wire wound resistor'
}
non_e_waste_message = "This is non e-waste."

# Function to predict the class
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0])

    # Threshold for confident predictions
    if confidence < 0.5:
        return "Unable to confidently classify the image."

    # Check if it's e-waste or non-e-waste
    if predicted_class in e_waste_labels:
        return f"Detected E-Waste: {e_waste_labels[predicted_class]} (Confidence: {confidence:.2f})"
    else:
        return non_e_waste_message

# Example usage
img_path = 'logo-CEMP.jpg'  # Replace with your image path
result = predict_image(img_path)
print(result)
