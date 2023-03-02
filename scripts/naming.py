import os
import random

# Set the path to the input folder
input_folder = './before'

# Set the path to the output folder
output_folder = './after'

# Get a list of image files in the input folder
file_list = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

# Shuffle the file list
random.shuffle(file_list)

# Loop over each image file and rename it with a new unique name
for i, filename in enumerate(file_list):
    # Generate a new unique filename
    new_filename = 'others_{:04d}.jpg'.format(i+1)

    # Set the path to the input and output files
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, new_filename)

    # Rename the file
    os.rename(input_path, output_path)
