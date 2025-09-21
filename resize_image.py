import os
from PIL import Image

# Input file (your original image)
input_image = r"c:\Users\Sri Lakshmi\Downloads\rose.jpg"

# Output folder (create a new folder for resized images)
output_folder = r"c:\Users\Sri Lakshmi\Downloads\Resized_Images"

# Desired size
output_size = (800, 400)

# Create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open and resize the image
img = Image.open(input_image)
resized_img = img.resize(output_size)

# Save the resized image inside the output folder
output_path = os.path.join(output_folder, "rose_resized.jpeg")
resized_img.save(output_path)

print(f"✅ Resized image saved at: {output_path}")
