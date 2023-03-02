from PIL import Image
import os

folder_path = "./main"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        image_path = os.path.join(folder_path, filename)
        with Image.open(image_path) as img:
            width, height = img.size
            if width > 950 or height > 950:
                ratio = min(950/width, 950/height)
                new_width = int(ratio * width)
                new_height = int(ratio * height)
                img = img.resize((new_width, new_height))
                img.save(image_path)
