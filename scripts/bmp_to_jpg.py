import os
from PIL import Image

# set input and output folder paths
input_folder = "./before"
output_folder = "./after"

# create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop over all BMP files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".bmp"):
        # open the BMP image file
        bmp_path = os.path.join(input_folder, filename)
        bmp_image = Image.open(bmp_path)

        # convert the BMP image to a JPEG image
        jpeg_image = bmp_image.convert("RGB")

        # save the JPEG image with the same filename in the output folder
        jpeg_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        jpeg_image.save(jpeg_path)
