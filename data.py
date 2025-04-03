import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
base_dir = r"C:\Users\lenovo\OneDrive\Desktop\E-WASTE ANALYSIS AND PREDICTING RECYCLING METHOD\E-WASTE-ANALYSIS-AND-PREDICTING-RECYCLING-METHOD\nonewaste"  # Change this to your actual base directory path
output_dirs = ["train", "test", "val"]

# Create train, test, and val directories
for folder in output_dirs:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Get all class folders inside base_dir
class_folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f not in output_dirs]

for class_name in class_folders:
    class_path = os.path.join(base_dir, class_name)
    images = os.listdir(class_path)
    
    # Split images into train (50), test (25), val (25)
    train_imgs, test_val_imgs = train_test_split(images, train_size=50, random_state=42)
    test_imgs, val_imgs = train_test_split(test_val_imgs, test_size=0.5, random_state=42)
    
    # Create class directories in train, test, val
    for folder in output_dirs:
        os.makedirs(os.path.join(base_dir, folder, class_name), exist_ok=True)
    
    # Move files
    for img in train_imgs:
        shutil.move(os.path.join(class_path, img), os.path.join(base_dir, "train", class_name, img))
    for img in test_imgs:
        shutil.move(os.path.join(class_path, img), os.path.join(base_dir, "test", class_name, img))
    for img in val_imgs:
        shutil.move(os.path.join(class_path, img), os.path.join(base_dir, "val", class_name, img))

print("Dataset successfully split into train, test, and val directories!")
