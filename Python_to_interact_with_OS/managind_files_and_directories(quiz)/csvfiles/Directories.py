import csv
#the following command should be used in the terminal
#----cat software.csv 
#Output name,version,status,users
#MailTree,5.34,production,324
#CalDoor,1.25.1,beta,22
#Chatty Chicken,0.34,alpha,4
with open(software.csv) as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"],row["users"]))
"""
Here the code is opening the file and creating a DictReader to process our CSV data. Then, it’s going through the rows to access information in each row using the keys just like we would when accessing data in the dictionary. """

##Output:

#MailTree has 324 users

#CalDoor has 22 users

#Chatty Chicken has 4 users

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

"""Here the code creates a list of dictionaries with the data that we want to store. For this example, we want to store data about the users in our company and the departments that they work in. So here we have our list of dictionaries and each contain the keys, name, username and department. We now want to write this CSV file. So we first define the list of keys that we want to write to the file, then we open the file for writing. Next we created the DictWriter passing the keys that we had identified before, and then we call two different methods on the writer. The writeheader() method will create the first line of the CSV based on keys that we passed, and the writerows() method will turn the list of dictionaries into lines in that file. """
#the following command should be used in the terminal

#-- cat by_department.csv  

#This code displays the CSV file by_department.csv.
#Code output: 
#Name,username,department

#Sol Mansi,solm, IT infrastructure

#Lio Nelson,lion,User Experience Researcher

#Charlie Grey,greyc,Development

#https://docs.python.org/3/library/csv.html
#https://realpython.com/python-csv/