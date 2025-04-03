import tensorflow as tf

# Load the models
model1_path = r"E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/ewaste_mobilenetv2.h5"
model2_path = r"E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/E-Waste_Non-Ewaste_classifier.h5"

model1 = tf.keras.models.load_model(model1_path)
model2 = tf.keras.models.load_model(model2_path)

# Function to plot and save model architecture
def plot_model_architecture(model, model_name):
    tf.keras.utils.plot_model(model, to_file=f"{model_name}_architecture.png", show_shapes=True, show_layer_names=True)
    print(f"Model architecture saved as {model_name}_architecture.png")

# Generate and save architecture graphs
plot_model_architecture(model1, "E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/ewaste_mobilenetv2.h5")
plot_model_architecture(model2, "E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD/E-Waste_Non-Ewaste_classifier.h5")
