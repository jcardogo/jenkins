#!/usr/bin/env python3

#import os
import requests
import json

#Parameters
txt_file_path = 'supplier-data/descriptions/'
img_path = 'supplier-data/images/'
max_fruit_number = 10
index = 0
fruits = {}
keys = ['name', 'weight', 'description', 'image_name']

for fruit_number in range (1, max_fruit_number+1):
    #Create a dictionary to store the data
    
    #Parse the text file and create a dictionary
    with open (txt_file_path + f'{fruit_number:03d}' + '.txt') as description_file:
        print ('new execution', str(fruit_number))
        #Read the file line by line
        for ln in description_file:
            line = ln.strip()
            if 'lbs' in line:
                nline = line.split()
                wght = int(nline[0])
                fruits["weight"] = wght
                index += 1
            else:
                try:
                    fruits[keys[index]] = line
                    index += 1
                except:
                    fruits[keys[2]] = line
        fruits['image_name'] = img_path + f'{fruit_number:03d}' + '.jpeg' 
        index = 0
        print (fruits)
        #response = requests.post("http://35.185.213.128/fruits/", json=fruits)
        fruits.clear()
    #Increasing the number on fruit 
    fruit_number =+ 1
