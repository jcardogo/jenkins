import os
def new_directory(directory, filename):
    #Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    #Create the new file inside the new directory
    os.chdir(os.path.join(os.getcwd(), directory))
    with open(filename, "w") as file:
        pass    
    return os.listdir()
print(new_directory("PythonPrograms", "script.py"))