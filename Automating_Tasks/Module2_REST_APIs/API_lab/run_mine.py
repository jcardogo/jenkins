#! /usr/bin/env python3

import os
import requests

def list_files(directory):
    """
    Capture all files from the specific directory on a dictionary.
    Args:
        directory (str): Path to the directory.
    Returns:
        files (list): List of files on the directory.
    """
    files = []
    try:
        return[os.path.join(directory, file) for file in os.listdir(directory)]
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
directory = "/home/acardogo/Documents/TextSampler"
files = list_files(directory)
print (files)

def list_to_dict(file_list):
    """
    Create a dictionary from the content of each file.
    Args:
        file_list (list): List of paths to the files
    Returns: 
        dict: Dictionary of all feedbaks keeping title, name, date, and feedback as keys 
    """
    file_dict = []
    for file in file_list:
        try:
            with open(file, 'r') as f:
                #file_dict[file] = [line.strip() for line in f.readlines()]
                file_dict.append({"title":f.readline().rstrip("\n"), 
                            "name":f.readline().rstrip("\n"),
                            "date":f.readline().rstrip("\n"),
                            "feedback":f.readline().rstrip("\n")})
        except FileNotFoundError:
            print(f"FIle {file} not found.")
    return file_dict

file_dict = list_to_dict(files) 
print(list_to_dict(files))

def posting_feedback(url, file_dict):
    """
    Posting each feedback from the list of dictionaries created before
    Args:
        url (str): the url of the company's website
        file_dict (list): list of posting dictionaries with title, name, date, and feedback on it
    Returns: 
        N/A
    """
    for item in file_dict:
        resp = requests.post(url, json=item)
        if resp.status_code !=201:
            print(f"Something went wrong: {resp.text}")
            raise Exception('POST error status={}'.format(resp.status_code))
        print('Created feedback ID: {}'.format(resp.json()["id"]))
url = "http://127.0.0.1:80/feedback"
posting_feedback(url, file_dict)




