import os
def parent_directory():
    #Creating a relative path to the parent of the current working directory
    relative_parent = os.path.join(os.getcwd(), '..' )
    #return the ablosute path of the parent directory
    return os.path.abspath(relative_parent) 
print(parent_directory())