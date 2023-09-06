import os
import sys
from PIL import Image
'''This script converts JPG to PNG'''

#get image path
image_path = sys.argv[1]
output_path = sys.argv[2]

# check if folder exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# loop through image_path and convert to png
for filename in os.listdir(image_path):
    img = Image.open(f'{image_path}\{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_path}\{clean_name}.png', 'png')
    print (f'{filename} converted to png')
