import os
import datetime

def file_date(filename):
    #create the file in current directory
    with open(filename, "w") as file:
        pass
    timestamp = os.path.getmtime(filename)
    #convert the timestamp into a human readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp) 
    #return just the date portion
    #Hint: how many characters are in "YYYY-MM-DD"?
    return ("{}".format(str(date)[:10]))
print(file_date("new_quiz_file.txt"))
