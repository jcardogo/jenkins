import os
import csv

#Create a file with data in it
def create_file(filename):
    with open(filename, 'w') as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

####Managing data as DICTIONARY
#Read the files content and format the information about each row
def contents_of_file(filename):
    return_strign =""
    #call the function to create the file 
    create_file(filename)
    #open the file
    with open(filename) as data:
        #read the rows of the file as a dictionary
        reader = csv.DictReader(data)
        #process each row of the dictionary
        for row in reader:
            return_strign += "a {} {} is {} \n".format(row["color"],row["name"],row["type"])
    return return_strign
#call the function 
print(contents_of_file("flowers.csv"))


####Managing data 
#Read the files content and format the information about each row
def contents_of_file(filename):
    return_string=""
    #open the file  
    f = open(filename)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        name,color,type=row
        #format the return string for data rows only
        return_string += "a {} {} is {}\n".format(color,name,type)
    return return_string
#call function
print(contents_of_file("flowers.csv"))