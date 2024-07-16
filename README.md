# OCR Project with Python and Tesseract

This project demonstrates how to use Python with the Tesseract OCR engine to extract text from images. The script processes images in the `input_images` directory and saves the extracted text to the `output_texts` directory.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Script Explanation](#script-explanation)
  - [Setting Up Tesseract](#setting-up-tesseract)
  - [Preprocessing Images](#preprocessing-images)
  - [Performing OCR](#performing-ocr)
  - [Handling Exceptions](#handling-exceptions)
- [Examples](#examples)
- [License](#license)

## Introduction

Optical Character Recognition (OCR) is a technology used to convert different types of documents, such as scanned paper documents, PDFs, or images taken by a digital camera, into editable and searchable data. This project utilizes Tesseract, an open-source OCR engine, to perform text extraction from images using Python.

## Installation

1. **Install Tesseract-OCR**:
   - Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
   
2. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/ocr-project.git
   cd ocr-project

3. **Install Python Dependencies**:
   ```sh
   pip install pytesseract pillow

4. **Usage**
   - 1. Place your images in the input_images directory.

   - 2. Run the OCR script:
     ```sh
     python ocr_script.py
     ```

   - 3. The extracted text will be saved in the output_texts directory.


## Script Explanation

### Setting Up Tesseract

We begin by providing the path to the Tesseract executable:
```code
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
> **_NOTE:_** Make sure to give the correct path to your Tesseract executable file.

### Preprocessing Images

For this tutorial, we directly use the images without additionl preprocessing. However, for better accuracy, you can add image preprocessing steps like grayscale conversion, noise reduction, and thresholding.

###  Performing OCR

The script reads each image file, performs OCR using Tesseract, and writes the extracted text to a text file:
```code
for filename in os.listdir(input_dir):
    try:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)

            text = pytesseract.image_to_string(image)

            output_path = os.path.join(output_dir, filename + ".txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Extracted text from {filename} and wrote to {output_path}")
    except FileNotFoundError:
        print(f"Error: Image file not found: {image_path}")
    except Exception as e:
        print(f"An unexpected error occurred for {filename}: {e}")
```

### Handling Exceptions
The script includes exception handling to manage common errors:

* **FileNotFoundError**: Raised if the image file is not found.
* **General Exception**: Catches any other unexpected errors.


### Examples

#### Input Image
Place your image files in the input_images directory. Here’s an example image:


### Output Text
After running the script, the extracted text will be saved in the output_texts directory. For the example image, the output text might look like this:

```
This is a sample text extracted from the image.
```

### License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/iqra-1/python-ocr-project/blob/main/LICENSE.) file for more details.

## How to Use This README

1. **Replace Placeholders**: 
   - Replace `https://github.com/your-username/ocr-project.git` with your actual GitHub repository URL.

2. **Include Example Images**: 
   - Add a sample image in the `input_images` directory.
   - Adjust the example image link in the README if needed.

3. **Update License**: 
   - If you choose to include licensing information, ensure the `LICENSE` file is added to your repository.

This README file provides a comprehensive tutorial for your project, guiding users through installation, usage, and understanding of the code. It also includes instructions for licensing, making it a professional and user-friendly documentation for your project.


