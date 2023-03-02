import os
import json

# Set the path to the folder containing the JSON files
folder_path = './main'

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a JSON file
    if filename.endswith('.json'):
        # Load the JSON file
        file_path = os.path.join(folder_path, filename)
        with open(file_path) as f:
            data = json.load(f)
        
        # Iterate over the list of dictionaries
        for d in data:
            # Get the bounding_box list
            bbox = d['bounding_box']
            # Swap the first and third elements
            bbox[1], bbox[3] = bbox[3], bbox[1]
        
        # Write the modified data back to the same file
        with open(file_path, 'w') as f:
            json.dump(data, f)
