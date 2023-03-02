import os
from PIL import Image

# set input and output folder paths
input_folder = "./before"
output_folder = "./after"

# create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop over all PNG files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # open the PNG image file
        png_path = os.path.join(input_folder, filename)
        png_image = Image.open(png_path)

        # convert the PNG image to a JPEG image
        jpeg_image = png_image.convert("RGB")

        # save the JPEG image with the same filename in the output folder
        jpeg_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        jpeg_image.save(jpeg_path)
