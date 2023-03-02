import os
import json
from paddleocr import PaddleOCR

os.environ["KMP_DUPLICATE_LIB_OK"]="True"

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Path to the input images folder
input_folder = './images'

# Path to the output JSON files folder
output_folder = './images_output'

# Recursively loop through all files in the input folder
for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.png'):
            
            # Load the image
            image_path = os.path.join(root, filename)

            # Perform OCR on the image
            result = ocr.ocr(image_path, cls=True)

            # Create a dictionary to store the results
            results_dict = []

            # Loop through each detected text and add it to the dictionary
            for text in result[0]:
                top = min(text[0][0][1],text[0][1][1],text[0][2][1],text[0][3][1])
                bottom = max(text[0][0][1],text[0][1][1],text[0][2][1],text[0][3][1])
                left = min(text[0][0][0],text[0][1][0],text[0][2][0],text[0][3][0])
                right = max(text[0][0][0],text[0][1][0],text[0][2][0],text[0][3][0])
                results_dict.append({
                    'word':text[1][0],
                    'bounding_box':[left, top, right, bottom]
                })

            # Create the output directory if it doesn't exist
            output_subdir = os.path.relpath(root, input_folder)
            os.makedirs(os.path.join(output_folder, output_subdir), exist_ok=True)

            # Save the dictionary as a JSON file in the same directory structure as the input image
            json_path = os.path.join(output_folder, output_subdir, filename.replace('.jpg', '.json').replace('.png', '.json'))
            with open(json_path, 'w') as f:
                json.dump(results_dict, f)
