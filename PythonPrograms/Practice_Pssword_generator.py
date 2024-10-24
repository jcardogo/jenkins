import csv #to read and write CSV files
import secrets #to generate a random password for each user
import subprocess #this calls the useradd command, which creates and adds each user account.
from pathlib import Path # to locate the data files for each iser account.
cwd = Path.cwd() /"/home/alejandrocardoso" #cwd for "current working directory" and identify the path of python directory as a string
with open(cwd / "users_in.csv", "r") as file_input, open(cwd / "users_out.csv", "w") as file_output: #resource management creating alias for the files used
    reader = csv.DictReader(file_input) #Use "DictReader" so that each row in the file is read into dict() with the field name and value, like this: {"username": "amanda", "password": "", "real_name": "Amanda Alonso"}
    writer = csv.DictWriter(file_output,fieldnames=reader.fieldnames) #Create a "DicWriter" and use the same field names from the input
        writer.writeheader()  #copying the header from input file
        for user in reader: #loop to run through each from the input file
            user["password"] = secrets.token_hex(8) #generate a random password of eight hex bytes, which equals 16 characters in total
            useradd_cmd = ["/sbin/useradd", #run the /sbin/useradd command to create each user
                           "-c", user["real_name"],
                           "-m",
                           "-G", "users",
                           "-p", user["password"],
                           user["username"]]
            subprocess.run(useradd_cmd, check=True) #Check "check=True" parameter cause the script to exit with a "CalledProcessError" if the command fails for any reason.
        writer.writerow(user) #Write the record back to the output file, incluiding the password. When running the code, the new user accounts and passwors are generated into a new CSV file 
    
     
