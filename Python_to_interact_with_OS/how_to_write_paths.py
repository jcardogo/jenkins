
######NOtes of the course
#import os
#---Windows file directory
#C:\my-directory\target-file.txt
#---Windows file directory written in Python
#C:/my-directory/target-file.txt.
#---Windows file directory on Python when using \
#C:\\my-directory\\target-file.txt
#---CWD command:
#os.getcwd()
#CWD command for external files:
#outputs['current_directory_before'] = os.getcwd()
#outputs['file_and_directories'] = os.listdir()
#outputs['path_value'] = os.environ.get('PATH')
#Implementation
import os #this module provides a funtion to interact with operatinve System
os.remove("novel.txt") #This code removes the file novel.txt
os.remove("Novel.txt") #This code will throw a file not found error. You cannot remove a file that doesn’t exist.
os.rename("first_draft.txt", "finished_masterpiece.txt") #This code can be used to rename a file 
os.path.exists("fnished_masteroiece.txt") #This code checks whether or not a file exists. If the file exists it will return True. If the file does not exist it will return False.
os.path.exists("userlist.txt")
#More File Information
os.path.getsize("spider.txt")#This code will provide the file size
import datetime
timestamp = os.path.getmtime("spider.txt")#This code show a long numer representing timestamps of the most recent modification
datetime.datetime.fromtimestamp(timestamp)#This code will provide the date and time for the file in an easy-to-understand format
os.path.abspath("spider.txt") #This code takes the file name and turns it into an absolute path
###
print(os.getcwd())#This code snippet returns the current working directory.
os.mkdir("new_dir")#The os.mkdir("new_dir") function creates a new directory called new_dir
os.chdir("new_dir")#This code snippet changes the current working directory to new_dir.
os.getcwd()#The second line prints the current working directory.
os.mkdir("newer_dir") #This code snippet creates a new directory called newer_dir. 
os.rmdir("newer_dir") #The second line deletes the newer_dir directory.
os.listdir("website") #This code snippet returns a list of all the files and sub/directories in the directory.
dir = "website" # creating a string variable named dir
for name in os.listdir(dir): # iterate all the names (strings) of the directory
    fullname = os.path.join(dir, name) #storing each name on a string variable called fullname
    if os.path.isdir(fullname): #checking if the fullname correspond to a directory
        print("{} is a directory".format(fullname)) #print the name and mentinoning that it is a directory
    else:
        print("{} is a file".format(fullname)) #in other case it will print the name mentioning that it is a file