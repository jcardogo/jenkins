#!/usr/bin/env python3
from PIL import Image

#Open the image file
image_number = 1
print (f'{image_number:03d}')
while image_number  <= 10:
    #Construct image ID with leading zeros
    image_id = 'supplier-data/images/'+ str(f"{image_number:03d}") + '.tiff'
    
    try:
        img = Image.open(image_id)
        print(img)
        # COnvert the image from RGBA to RGB
        rgb_img = img.convert('RGB')
        resized_img = rgb_img.resize((600,400))
        #Save the converted image
        resized_img.save ('supplier-data/images/' + str(f"{image_number:03d}") + '.jpeg')
    except FileNotFoundError:
        print(f"Error: FIle '{image_id}' not found")
    #Increment image number
    image_number += 1

