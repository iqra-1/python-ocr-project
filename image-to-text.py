import pytesseract
from PIL import Image
import os

# Providing the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Setting the input and output directories
input_dir = "input_images"
output_dir = "output_texts"

# Creating the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Looping through all image files in the input directory
for filename in os.listdir(input_dir):
    # Adding more extensions as needed for images.
    if (
        filename.endswith(".jpg")
        or filename.endswith(".jpeg")
        or filename.endswith(".png")
    ):
        # Opening the image file
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)

        # Performing OCR
        text = pytesseract.image_to_string(image)

        # Writing the extracted text to a file in the output directory
        output_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_dir, output_filename)
        # output_path = os.path.join(output_dir, filename + ".txt")
        with open(output_path, "w") as f:
            f.write(text)

        print(f"Extracted text from {filename} and wrote to {output_path}")
