import requests #testing if the module request (use to interacnt with web servers) is installed
import arrow #checking if module arrow (create a date object from a string) 
date = arrow.get('2020-01-18', 'YYYY-MM-DD') #saving the string in date format to be accesible
date.shift(weeks=+6).format('MMM DD YYY') #adding 6 weeks to the date and defininf print format
import PIL.Image #Python Imaging Library to interact with images, and image module from it
image = PIL.Image.open("<Name of the file>.jpg")
print(image.size)
print(image.format)
import pandas #Used for data analysis
visitors = [ 1234, 25635, 25645, 2579, 89563 ] #inserting some data about last 5 days attendance
n_errors = [ 256, 269, 875, 451, 569 ] #inserting some info about last 5 days errors
df = pandas.DataFrame( {"visitors": visitors, "n_errors": n_errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri" ]) #Creating a Dataframe adding indexes 
print(df) #printing data 
df["n_errors"].mean() #calculating the mean of all errors
########How to run a Python script

