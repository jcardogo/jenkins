#!/usr/bin/env python
import os
import PIL

from PIL import Image

def capture_tiffiles(directory):
    """
    Capture all .tif files from the specific directory.
    Args:
        directory (str): Path to the directory.
    Returns:
        list of .tif file paths.
    """
    tif_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".tif"):
            tif_files.append(os.path.join(directory, filename))
    return tif_files
"""
# Example usage
directory = "/path/to/your/directory"
jpg_files = capture_jpg_files(directory)
print(jpg_files)
"""    

def process_jpg_files(file_paths):
    """
    Process each .jpg file by rotating, resizing, and saving the new image.
    Arguments:
        file_path (list): list of .jpg file paths.
    """
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        output_filename = f"processed_{filename}"
        output_path = os.path.join(os.path.dirname(file_path), output_filename)
        im = Image.open(file_path)
        im.rotate(90).rezise((128,128)).save(output_path)
        print(f"Processed {filename} and saved as {output_filename}")
"""
# Example usage
directory = "/path/to/your/directory"
jpg_files = capture_jpg_files(directory)
process_jpg_files(jpg_files)
"""
