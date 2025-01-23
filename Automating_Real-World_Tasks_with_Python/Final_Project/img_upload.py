#!/usr/bin/env python3

import requests

#This example shows how a file can be uploaded using the Python Request module

max_image_number = 10
url = "http://localhost/upload/"
for image_number in range(1, max_image_number+1):
    with open('supplier-data/images/' + str(f"{image_number:03d}") + '.jpeg', 'rb') as opened: #In this script, we are going to upload a sample image named icon.sheet.png.
        r = requests.post(url, file={'file': opened})