#data types

#def to_celsius(x: any) -> any
#		‘’’Convert Farenheit to Celsius’’’
#		return (x-32) * 5/9
#
#	to_celsius(75)


def to_celsius(x):
    '''Convert Fahrenheit to Celsius'''
    return (x-32) * 5/9
print(to_celsius(75))

print (7+8)

print ("Hello" + "World")

#error test
#print (7+"8")

print (type(2))
print (type("Angela"))
print (type(2.5))
print ("*******Variables*****")

##Variables annotated by type
import typing 
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10 
# Define a variable of type float
y: float = 1.23
#Define a variable of type tuple
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}
# printing all variables
print (z)
print (x)
print (y)
print (list_of_numbers)
print (dictionary)
print (set_of_numbers)
print ("*****end_of_variables")
# Nice variables practice

# Skill Group 1 use variables to store valueas and use basic arithmetic operation to finally use explicit conversion to change data type from float to string
hotel_room = 401
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests
print("Each person need to pay: " + str(share_per_person))

# Skill Group 2 Output multiple string variables on a single line to form a sentence, use the plus (+) connector or a comma ro connect strings in a print() function, and create spaces between variables in a print() funtion.
print ("******Skills 2****")
salutation = "Dr."
fist_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
print (salutation + " " + fist_name + " " + middle_name + " " + last_name + ", ")
print (salutation, fist_name, middle_name, last_name,",", suffix)

# Skill Group 3 Resolve TypeError caused by a data type mismatch issue using an explicit conversion function
print ("*******Skills 3*******")
#print ("5 * 3 =" + (5*3))
print ("5 * 3 = " + str (5*3))

#Skills group 4 Revolde a ZeroDivisionError caused by an attempt to divide by 0
print ("*****Skills 4****")
numerator = 7
denominator = numerator
result = numerator / denominator
print (result)

#####Functions
print ("*****Expressions and Variables")
print ("****Functions******")
print ("---use of def --")
def greeting(name) :
    print ("Welcome, " + name)
greeting ("Kay")
greeting ("Cameron")
greeting ("Alejandro")
print ("-- use of def on a arrangement")
def greeting (name, department) :
    print ("Welcome, " + name)
    print ("You are part of " + department)
greeting ("Blake", "Software engineering")
greeting ("Ellis", "Hardware engenieering")
#BUilt-in functions
print ("****Built-in functions")
month = "September"
print ("Investigate failed login attempts during", month, "if moore than", 100)
print (type("This is a string"))
number = 12
string_representation = str(number)
print(string_representation)
#sorted
print ("--- Use of stored")
time_list = [12, 2, 32, 19, 57, 22, 14]
print (sorted(time_list))
print (time_list)
#max and min
print ("--- use of max() and min()")
print (max(time_list))
print (min(time_list))
#Returning Values
print("***Returning Values")
def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("the sum of both areas is: " + str(sum))
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5000)
print("5000 seconds are equal to:", hours, "hour", minutes, "minutes, and", seconds, "seconds")
print("----greeting--")
def greeting (name):
    print ("Welcome, " + name)
result = greeting("Christine")
print(result)
#Code_Reuse
print ("---Code Reuse")
name = "kay"
number = len(name) * 9 #len stanfing for length
print ("Hello " + name + ". Your lucky number is " + str(number))
name = "cameron"
number = len(name) * 9 #len standing for length 
print ("Hello " + name + ". Your lucky number is " + str(number))
#impoving the same code on simpler 
def lucky_number (name):
    number = len(name) * 9
    print ("Hello " + name + ". Your lucky number is " + str(number))
lucky_number("Kay")
lucky_number("Cameron")
##Code_Style
print ("----Code Style")
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print (z)
calculate(5) #expected output 78.5
def circle_area (radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print (area)
circle_area(5) #expecter output 78.5
#Functions review
print ("---Functions Review")
print ("#Skill 1")
def find_total_days(years, months, days):
    my_days = (years*365) + (months*30) + days
    return my_days
print ("Total days: ", find_total_days(2,5,23))
print ("#skill 2")
def convert_volume(fluid_ounce) :
    ml = fluid_ounce * 29.5
    return ml
x = 2
print("The volume in ounces is " + str(x))
print("The volume in mililiters is " + str(convert_volume(x)))
print("The double of volume in mililiters is " + str(convert_volume(x)*2))
print("Skill 3")
#####Conditionals
print (" ----CONDITIONALS")
print (10>1) #True
print ("cat" == "dog") #False
x = "cat"
print ("cat" == x)
print (1 != 2) #True
##### Equality == and not equality !=
print ("--Equality and not equality")
print ("a string" == "a string")
print ("4 + 5" == 4 + 5)
print ("rabit" != "frog")
event_city = "Shanghai"
print (event_city != "Shanghai")
print ("three" == 3)
### Greater than > and less than < 
print ("--- Greater than and less than")
print ("Is Wednesday greater than Friday?: " + str("Wednesday" > "Friday"))
print ("Is Brown less than brown?: " + str("Brown" < "brown"))
print ("Is sunbathe greater than suntan?: " + str("sunbathe" > "suntan"))
print ("Is Lima less than Lima?: " + str("Lima" < "Lima"))
print ("Is five less than 6?: " + str("five" < str(6)))
### Greater than or equal to >= and less than or equal to <= 
print ("---- Greater than or equal and less than or equal to operator")
var1 = "mycomputer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
print ("Is \"mycomputer\" greater than or equal to \"my chair\"? Result: ", var1)
print ("Is \"Spring\" less than or equal to \"Winter\"? Result", var2)
print ("Is \"pinapple\" less than or equal to \"pineaple\"? Result: ", var3)
#Logical Operators
print("---- Logical Operators: and, or, not")
print((6*3 >= 18) and (9+9 <= 36/2))
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")
Country = "United States"
city = "New York City"
print((15/3 < 2+4) or (0 >= 6-7)) #True or True = True
print(Country == "New York City" or city == "New York City") # False or True = True
print(16 <= 4**2 or 9**(0.5) != 3) #True or False = True
print("B_name" > "C_name" or "B_name" < "A_name") # False or False = False
# Not Example 1:
print("--use of not")
x= 2*3 >6
print("The value of x is:")
print(x)
print("") #Prints a blank line
print("The inverse value of x is: ")
print(not x)
#Not Example 2
today = "Monday"
print(not today == "Tuesday")
#Branching with if statements
print("--- Branching with if statement:")
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("The name is fine")
hint_username("Mario")    
#use of if Example2 without "else" word on it 
def is_even(number):
    if number % 2 == 0: #% is function modulo, just save the integer part of the result 
        return True
    return False
    #This code has no output
print("--elif statement")
def hint_username(username):
    if len (username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")
hint_username("Mario")
#Same code now using elif
def hint_username(username):
    if len(username)< 3:
        print("Invalid username. must be at least 3 characters long")
    elif len(username)>15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")
#Copied from google course
print("----Use of if, elif else on course ")
# This function accepts one variable as a parameter
def translate_error_code(error_code):
 
# The if-elif-else block assesses the value of the variable
# passed to the function as a parameter. The if statement uses 
# the equality operator == to test the value of the variable.
# This test returns a Boolean (True/False) result.
    if error_code == "401 Unauthorized":
# If the comparison above returns True, then the indented 
# line(s) inside the if-statement will run. In this case, the
# action is to assign a string to the translation variable.
# The remainder of the if-elif-else block will not run.
# The Python interpreter will skip to the next line outside of 
# the if-elif-else block. In this case, the next line is the 
# return value statement.  
        translation = "Server received an unauthenticated request"
 
# If the initial if-statement returns a False result, then the
# first elif-statement will run a different test on the value
# of the variable.
    elif error_code == "404 Not Found":
# If the first elif-statement returns a True result, then the
# indented line(s) inside the first elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Requested web page not found on server"
 
# If both the initial if-statement and the first elif-statement 
# return a False result, then the second elif-statement will
# run.
    elif error_code == "408 Request Timeout":
# If the second elif-statement returns a True result, then the
# indented line(s) inside the second elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Server request to close unused connection"
 
# If the conditional tests above do not produce a True result
# then the else-statement will run. 
    else:
        translation = "Unknown error code"
# The if-elif-else block ends.

# The next line outside of the if-elif-else block will run
# after exiting the block. In this case, the next line returns
# the output from the if-elif-else block.
    return translation

# The print() function allows us to display the output of the
# function. To call a function in a print statement, the syntax
# is print(name_of_function(parameter))
print(translate_error_code("404 Not Found"))

# Expected output:
# Requested web page not found on server

#### Example2
print("-- Example2 if,elif,else")
number = 25
if number <= 5:
    print("The number is 33.")
elif number < 32 and number >= 6:
    print ("The number is less than 32 and greater than 6.")
else:
    print("The number is " + str(number))

### Example 4
print("-- Example 4")
def round_up(number):
    x=10
    whole_number = number // x
    remainder = number % x
    if remainder >= 5:
        return x*(whole_number+1)
    return x*whole_number
print(round_up(35)) 

print("---to test")
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize / block_size
    print("full_blocks", str(full_blocks))
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    print ("Partial_blocks", partial_block_remainder)
    if partial_block_remainder > 0:
        return block_size * (int(full_blocks)+1) 
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


###Study Guide: Module 2
print("Study_Guide:Module2")
print("--Group1: task remainder")
def task_reminder(time_as_string):
    if time_as_string == "8:00 a.m.":
        task = "Check overnigth backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    else:
        task = "Provide IT Support to employees"
    return task
print(task_reminder("10:00 a.m."))
print(task_reminder("8:00 a.m."))
print(task_reminder("8:30 a.m."))
print(task_reminder("11:30 a.m."))
print(task_reminder("12:00 m"))
print(task_reminder("5:30 p.m."))
print("--Group3: COmparison and logical operators")
def get_remainder(x,y):
    if x == 0 or y == 0 or x == y:
        remainder = "you are great"
    else:
        remainder = (x % y) / y
    return remainder 
print(get_remainder(10,3))
print(get_remainder(0,10))
print(get_remainder(2,2))
print(get_remainder(500,6))
#######MODULE 3 LOOPS
print("#######MODULE 3 - LOOPS")
print("--My first while loop")
x = 0
while x < 5:
    print("Not there yet, x= " + str(x))
    x = x+1
print("x= " + str(x))
print("-- Exersise1")
def attempts(n):
    x=1
    while x<=n:
        print("Attempt " + str(x))
        x+= 1
    print("Done")
attempts(5)
#username = get_username()
#while not valid_username(username):
#    print("Invalid username")
#    username = get_username()
#Why initializing a value matters
print("--- Importance of initializing a variable")
my_variable=5
while my_variable < 10:
    print("Hello")
    my_variable += 1
print("Example2")
x= 1
sum = 0
while x <10:
    sum = sum + x
    x += 1

product = 1
x=1
while x < 10:
    product = product * x
    x += 1
print (sum, product)
# Infinite loops and how to break them
print("****INFINITE LOOPS AND HOW TO BREAK THEM*****")
while x % 2 == 0:
    x = x / 2
#No output
if x != 0:
    while x % 2 == 0:
        x = x / 2
#No output
while x != 0 and x % 2 == 0:
    x = x / 2
#No output   
#while True:
#    do_something_cool()
#    if user_requested_to_stop():
#        break
#This code will give an error becouse do_something_cool is not defined
print("While loops examples")
multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1 # I had a typo here using =+ instead of += theat lead the code to a infinite loop 
    result = multiplier * 5
print("Done")
# This while loop prints the multiples of 5 between 1 and 50. The
# "multiplier" variable is initialized with the starting value of 1. 
# The "result" variable is initialized with the value of the 
# "multiplier" variable times 5. 

# The while loop specifies that the loop must iterate while it is True
# that the "result" is less than or equal to 50. Within the while loop, 
# the code tells the Python interpreter to print the value of the 
# "result" variable. Then, the "multiplier" is incremented by 1 and the
# "result" is assigned the new value of the "multiplier" times 5. 

# The end of the while loop is indicated by the indentation of the next 
# line of code moving one tab to the left. At this point, the Python
# interpreter automatically loops back to the beginning of the while
# loop to check the condition again with the new value of the "result"
# variable. When the while loop condition becomes False (meaning
# "result" is no longer less than or equal to 50), the interpreter exits
# the loop and reads the next line of code outside of the loop. In this 
# case, that next line tells the interpreter to print the string "Done". 

# Click the "Run" button to check the result of this while loop.
print("---LOOPS *Coding Skills 1")
print ("Count of factors for a number")
#This function counts the number of integer factors for a 
#"given_number" variable, passed through the functions's parameters.
# The "count" return value includes the "given_number" itself as a 
#factor (n*1).
def count_factors(given_number):

    #To include the "given_number" variable as a "factor", initialize 
    #the "factor" variable with the value 1 (if the "factor" variable
    #were to start at 2, the "given_number" itself would be excluded).
    factor = 1
    count = 1
    #this "if block will run the "given_number equals 0.
    if given_number == 0:
        return 0
    #THe while loop will run while the "factor" is still less than 
    #The "given_number" variable.
    while factor < given_number:
        #THis "if "block checks if the "given_number" can be divided by
        #the "factor" variable without leaving a remainder. THe modulo
        #operator % is used to test for a remainder.
        if given_number % factor == 0:
            count += 1
        #When exiting the if block, incement the "factor" variable by 1
        #to divide the "given_number" variable by a new "factor" value
        #inside eht while loop.
        factor += 1
    #When the interpreter exist either the while loop or the top if
    #block, it will return the value of the "count" variable 
    return count

print(count_factors(0)) #Count value should be 0
print(count_factors(3)) #SHould count 2 factors (1X3)
print(count_factors(10)) #Should count 4 factors (1x10, 2X5)
print(count_factors(24)) #SHould count 8 factors (1x24, 2x12, 3x8, and 4x6)
#######
print("-----Skill 2")
def addition_table(given_number):
    iterated_number =1 
    my_sum = 1
    while iterated_number <= 5:
        my_sum = given_number + iterated_number
        if my_sum >20:
            break
        print (str(given_number), "+", str(iterated_number), "=", str(my_sum))
        iterated_number += 1
addition_table(5)
addition_table(17)
addition_table(30)
######
print("************* use of a FOR loop ***********")
for x in range (5):
    print (x)
friends =['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi ", friend)
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum:", str(sum), "- Average:", str(sum/length))
### More for loop examples
print("More for loop examples")
product = 1
for n in range (1, 10):
    product = product * n
    print(product)
print("--- Temperature converter from farenheit to Celsius:")
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x)) 
print("THe Range() function")
#for n in range (start, stop, step):
#    print(n)
for n in range(3):
    print (n)
for n in range(3+1):
    print (n)
for n in range(2*5,0,-2):
    print(n)
#Nested for loops
print("-Nested for loops")
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print (home_team, "vs", away_team)
#for element in long_list:
#    do_something(element)
#for element1 in long_list:
#    for element2 in long_list:
#        do_something(element1, element2)
## Looping over a string
greeting = 'Hello'
for char in greeting:
    print(char)
for i in range (len(greeting)):
    print(i)
greeting = 'Hello'
index = 0
while index < len (greeting):
    print(greeting[index])
    index += 1
greeting = 'Hello'
index = 0
while index < len(greeting):
    print (greeting[index:index+1])
    index += 1 
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print (squared_numbers)

## Slice and Join Strings

string1 = "Greetings, Earthlings"
print(string1[0]) # Print "G"
print(string1[4:8]) # Prints "tring"
print(string1[11:]) # Prints "Earthlings"
print(string1[:5]) # Prints "Greet"
print(string1[-10:]) # Prints "Earthlings" again
print(string1[55:]) # Prints""
print(string1[0::2]) #Prints "Getns atlns"
print(string1[::-1]) #Prints "sgilhtraE, sgniteerG"
print("Hello", "world") #Prints "Hello world"
greetings = ["Hello", "world"]
print(" ".join(greetings)) #Prints "Hello world"
#You can also concatenate a combination of strings and variables like in the following
name = "Alice"
print ("Hello, " + name + "!") #Prints "Hello, Alice!"
#How to combine slicing and joining strings
##The first 3 digits are the area code:
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    ##The next 6 digits are called the "exchange":
    exchange = phonenum[3:7]
    #The next 3 digits are the line number:
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
print(format_phone("31026590570"))
###What is recursion
print("--Use of recursion")
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning", str(result), "for factorial of", str(n))
    return result

print(factorial(4))    
#####Example of using recursion for automating the count of file on a machine
#def recursive_function(parameters):
#   if base_case_condition(parameters):
#       return mase_case_value
#   recursive_function(modified_parameters)
print("Module3-----StudyGuide---skill1")
print("--Count by 10")
def count_by_10(end):
    count = " "
    for number in range (0,end+1,10):
        count += str(number) + " "
    return count.strip()
print(count_by_10(100))
print("---Creating a matrix")
def matrix(initial_number, end_of_first_row):
    n1 = initial_number
    n2 = end_of_first_row+1
    for column in range(n1, n2):
        for row in range(n1, n2):
            print (column*row, end=" ")
        print()
matrix(1,4)
#print("--Predicting final number of a nested loop")
#for outer_loop in range(10):
#    for inner_loop in range (outer_loop):
#        print (inner_loop)
print("-Skill2:while")
print("while to print a secuence of numbers")
starting_number = 18
while starting_number >= 0:
    print(starting_number, end=" ")
    starting_number-=3
print("while to count the number of digits in a numeric value")
def x_figure(salary):
    tally = 0
    if salary == 0:
        tally += 1
    while salary >= 1:
        salary = salary/10
        tally += 1
    return tally
print("The CEO has a", str(x_figure(23000000)), "-figure salary.")

x = 1
sum = 0 
while x <= 10:
    sum += x
    x += 1
print(sum)
######MODULE4####################
print("What is a string")
name = "Sasha"
color = 'Gold'
# place = "Cambridge' will throw an error
pet = ""
print( "Name:", name + ", favorite color:", color)
print("example " * 3)
pet = "looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooog cat"
print(len(pet))
#Parts of a string
name = "Jaylen"
print (name[1])
print (name[0])
print (name[5])
# print (name[6]) throw an error becouse there is no character on spot 6
text = "Random string with a lot of characters"
print(text[-1])
print(text[-2])
color = "Orange"
print(color[1:4]) # print characters from 1 to 4 on the string
fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])
#replacing one character on a string
message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)
#function .index
pets = "Cats & Dogs"
print("Index of '&':", pets.index("&"))
print("Index of 'C':", pets.index("C"))
print("Index of 'Dog':", pets.index("Dog"))
print("Index of 's':", pets.index("s"))
print("Dragons" in pets)
print("Cats" in pets) #boolean to check strings
#
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_domain("jcardogo@gmail.com", "gmail.com", "hotmail.com"))
#More string methods
print("---More string methods")
print("Mountains".upper()) 
print("Mountains".lower())
answer = "YES"
if answer.lower() == "yes":
    print("User said yes")
print(" yes ".strip()) # to get rid of spaces, tabs or nule characters
print(" yes ".strip())
print(" yes".lstrip())
print(" yes ".rstrip())
print("The number of time e occurs in this string is 4".count("e"))
print("Forest".endswith("rest"))
print("Forest".isnumeric())
print("123456".isnumeric())
print(int("12345")+int("678910"))
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
print("This is another example".split())
###Formating strigns
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)))
price = 7.5
with_tax = price *1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
#String Reference guide
print("----String Reference guide")
print(len("abcde")) 
for c in "abcde": print(c)
print("abc" in "abcde")
print("def" in "abcde")
print("abcde"[2])
print("abcde"[-1])
print("abcde"[0:2])
print("abcd"[2:])
print("AaBbCcDdEe".lower())
print("AaBbCcDdEe".upper())
print("     Hello      ".lstrip())
print("     Hello      ".rstrip())
print("     Hello      ".strip())
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))
print("12345".isnumeric())
print("-123.45".isnumeric())
print("xyzzy".isalpha())
print(test.split()) 
test1 = "How-much-wood-would-a-woodshuck-chuck"
print(test1.split("-"))
print(test.replace("wood", "plastic"))
print("-".join(test.split()))
#Here are the items in the customer's basket. Each item is a tuple
#of (item name, weight, price per pound).
#
print("")
print("----Welcome to the new BASKET SUPERMARKET -----")
for times in range (2):
    print(" ")
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
]

#Calculate the total price of each item (weigth times price per pound)
# and add the up to get a subtotal.
# 
subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)

#Now calculate the sales tax and total bill.
#  
tax_rate = 0.06625
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt
#Print the receipt for the customer.
#
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("total:", total)
print("Best way to print--")
print("Subtotal:  ${:>4.2f}".format(subtotal))
print("Sales Tax: ${:>4.2f}".format(tax_amt))
print("Total:     ${:>4.2f}".format(total))

output = "You are buying {} punds of {} at {} per pund.".format(weight, fruit, unit_price)
print(output)

# Print the receipt for the customer. The format string ":10,.2f" 
# works as follows:
#   - ":10" makes the output 10 characters wide.
#   - "," inserts thousands separators between groups of digits.
#   - ".2" limits the output to two digits after the decimal.
#   - "f" tells Python to expect a floating-point number.
#
print("Copied from course")
print("Subtotal:     ${:10,.2f}".format(subtotal))
print("Sales Tax:    ${:10,.2f}".format(tax_amt))
print("Total:        ${:10,.2f}".format(total))

#########Formatted string literals
print("----------------Formatted string literals f'{}'")
name="Micah"
print(f'Hello {name}')
item="Purple Cup"
amount=5
price=amount*3.25
print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')
#####Study Guide:Strings
print("----Study Guide; STRINGS")
print("#Skills group1: mirrored_string")
def mirrored_string(my_string):
    forwards = ""
    backwards = ""
    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character + backwards
    if forwards.lower() == backwards.lower():
        return True
    return False
print(mirrored_string("12 Noon"))
print(mirrored_string("Was it a cat or a cat I saw"))
print(mirrored_string("'eve, madam Eve"))
print("#Skills group 2: converter_weigth")
def convert_weigth(ounces):
    pounds = ounces/16
    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result
print(convert_weigth(12))
print(convert_weigth(50.5))
print(convert_weigth(16))
print("#Skill group 3: Username")
def username(last_name, birth_year):
    return("{}{}".format(last_name[0:3],birth_year))
print(username("Ivanov","1985"))
print(username("Rodriguez", "2000"))
print(username("Deng", "1991"))
print("#Skill group 4: replace_dates")
def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule
    return schedule
print(replace_date("Last year's annual report will be released in March 2023", "2023", "2024"))
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
print(replace_date("The convention is scheduled for October", "October", "June"))
#####Use of lists
print("#########Use of lists ##############")
x=['Now', 'we', 'are', 'cooking!']
print(x)
print(type(x))
print(len(x))
print("are" in x)
print(x[0])
print(x[3])
print(x[len(x)-1])
print(x[1:3])
print(x[:2])
print(x[2:])
#Introduction to lists
print("---Introduction to lists:")
fruits = ['Pineapple', "Banana", 'Apple', 'Melon']
fruits.append('Kiwi') #used to add a element to a secuenced list at the end
print(fruits)
fruits.insert(0, 'Orange') #Used to add one element on a specific index location on the secuenced list
fruits.insert(25, 'Peach')
print(fruits)
fruits.remove('Melon')
print(fruits)
fruits.pop(3)
print(fruits)
fruits[2] = "Strawberry"
print(fruits)
#Review
print("Review of lists")
fullname = ('Grace', 'M', 'Hopper')
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours *3600 ) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(type(result))
hours, minutes, seconds = result
print(hours, minutes, seconds)
hours, minutes, seconds = convert_seconds(10000)
print(hours, minutes, seconds)
#Iterating over lists and tuples
print("--Iterating over lists and tuples")
animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for animal in animals:
    chars += len(animal)
print('Total characters: {}, Average length: {}'.format(chars,chars/len(animals)))
winners = ['Ashley', 'Dylan', "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
def full_emails(people):
    result =[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
print(full_emails([('alex@example.xom', 'Alex Diego'), ("SHay@example.com", "Shay Brandt")]))
print("------ Exercise ")
def skip_elements(elements):
	# code goes here
	new_elements = []
	for index, element in enumerate(elements):
		#print("{}, {} ".format(index + 1 , element))
		if index % 2 == 0:
		 new_elements.append(element)
	return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#List comprehensions
#option1
multiples = []
for x in range (1,11):
    multiples.append(x*7)
print(multiples)
#option2
multiples = [x*7 for x in range(1,11)]
print(multiples)
#languages
languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C']
lengths = [len(language) for language in languages]
print(lengths)
#example
z = [x for x in range(0,101) if x % 3 ==0]
print(z)
#exercise
print('Printing odd numbers function using comprehension list creation')
def odd_numbers(n):
	return [x for x in range(0, n+1) if (x+1) % 2 ==0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
#####Use loops for complex code and comprehention for simple code
print('Comprehension Examples')
#new_list = []
#for thing in list_of_things:
#    new_list.append(do_something(thing))
#Create a list of tuples where each tuple contains the number 1, 2 and 3
number = [(1,2,3) for n in range(5)]
print (number)
###Simple list comprehension
print("List comprehension result:")
print([x*2 for x in range(1,11)])
###Long form for loop
print("Long form code result:")
my_list = []
for x in range (1,11):
    my_list.append(x*2)
print(my_list)
###Comprehension with conditional statement
print("List comprehension result:")
print([x for x in range(1,101) if x % 10 == 0])
print("Long form code result")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)
#Practice exercise 
print('square exercise')
def squares(start, end):
    return [number**2 for number in range (start,end+1)]
print(squares(2, 3))
print(squares(1, 5))
print(squares(0, 10))
# Convert a list to a tuple
print('convert a list to a tuple')
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)
#Remember that altrhough parentheses are often used to define a tuple,
#they're not always necessary. The following syntax is also valid:
my_tuple = 1, 2, 3, "Rocko"
print(my_tuple)
# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])
#you can't change the tuple itself
# my_tuple[0] = 3 #This would raise a TypeError

#But you can modify the mutable elements with the tuple
print('Modifing the one mutable element on the list belonging to the tuple')
my_tuple[2][0] = 'x'
print(my_tuple)
###REturning multiple values from functions
print('Returning multiple values from functions')
def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b
result = calculate_numbers(10,2)
print(result)
# As above function has four aritmetic calculation the return can be asigned to a single variable result each one as a variable
print("unpacking result from tuple to a separated variable returned")
add_result, sub_result, mul_result, div_result = calculate_numbers(10,2)
print("add_result:", add_result)
print("sub_result:", sub_result)
print("mul_result:", mul_result)
print("div_result:", div_result)
#List Operations and methods skills
print('######List operations and methods skills:')
print("----Skill 1")
years = ['January 2023', 'May 2025', 'April 2023', 'August 2024', 'September 2025', 'December 2023']
print(years)
updated_years = []
for year in years:
    if year.endswith("2023"):
        new = year.replace('2023','2024')
        updated_years.append(new)
    else:
        updated_years.append(year)
print(updated_years)
print('----Skill 2')
def squares(start, end):
    return [n*n for n in range(start,end+1)]
print(squares(2, 3))
print(squares(1, 5))
print(squares(0, 10))
print('----Skill 3')
#using updated_years function to 
updated_years = [year.replace("2023","2031") if year[-4:] == "2023" else year for year in years]
print(updated_years)
print("----Skill 4")
#spliting strings 
def change_string(given_string):
    new_string = ""
    new_list = given_string.split()
    for element in new_list:
        new_string += element[1:] + "-" + element [0] + " "
    return new_string
print(change_string('1one 2two 3three 4four 5five'))
print('----Skill 5: string.join()')
def list_elements(list_name, elements):
    return 'The ' + list_name + ' list includes: ' + ', '.join(elements)
print(list_elements('Printers', ['Color Printer', 'Black and white printer', '3-D Printer']))
### map method
print('----Skill 6: map() method')
def add_one(number):
    return number + 1
numbers = [1, 2, 3, 4, 5]
result = map(add_one, numbers)
print(list(result))
#### zip()
print('Skill 7: zip() method')
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
#Use zip to combine the lists
combined = zip(names,ages)
#convers the zip object to a list to print the result
print(list(combined))
###########List practice quiz
print('---Exercise 1:')
filenames = ['program.c', 'studio.hpp', 'sample.hpp', 'a.out', 'math.hpp', 'hpp.out']
new_filenames = []
for filename in filenames:
    if filename.endswith('hpp'):
        #print(filename) check point
        new_filename = filename.replace('hpp', 'h')
        #print(new_filename) check point
        new_filenames.append(new_filename)
    else:
        new_filenames.append(filename)
print(new_filenames)
print('---Exercise 2:')
filenames = ['program.c', 'studio.hpp', 'sample.hpp', 'a.out', 'math.hpp', 'hpp.out']
new_filenames = [ filename.replace('hpp','h') if filename.endswith('hpp') else filename for filename in filenames]
print(new_filenames)
print('Exercise 3:')
def pig_latin(text):
    say = ""
    words = text.split(" ")
    for word in words:
        new_word = word[1:] + word[0] + "ay"
        print(new_word)
        say += new_word + " "
    return say
print(pig_latin('hello how are you'))
print(pig_latin("programming in python is fun"))
print('Exercise 6')
def biography_list(people):
    #people_tuple=tuple(people)
    for person in people:
        #person_tuple = tuple(person)
        name, age, profession = person
        print("{} is {} years old and works as {}".format(name, age, profession))
biography_list([("Ira",30,"a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")]) 
######## What is a Dictionary
x = {}
print(type(x))
file_counts = {"jpg":10, "txt":14, "cvs":2, "py":23}
print (file_counts)
print (file_counts ["txt"])
print("jpg" in file_counts)
print("html" in file_counts)
file_counts["cfg"] = 8 #adding a new element 
print(file_counts)
# data inside a dictionary is organized on pairs element-key
for extension in file_counts:
    print (extension) 
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extention".format(amount, ext))
print(file_counts.keys())
print(file_counts.values())
for value in file_counts.values():
    print (value)
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] =0
        result[letter] += 1
    return result
print (count_letters("aaaaaaaaaaaa"))
print (count_letters("tenant"))
print (count_letters("a long string with a lot of letters"))
####### Study guide: Dictionary Methods
pet_dictionary = {"dogs":["Yorkie", "Colie", "Bulldog"], "cats":["Persian", "Scotish Fold", "Siberian"], "rabbits":["Angola", "Holand loop", "Harlequin" ]}
print(pet_dictionary.get("dogs", 0))
#####Skills
print("------ Dictionaries Skills 1")
# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.
def sum_server_use_time(server):
    #Initialize the variable as a float data type, which will be used
    #to hold the sum  of the total hours and minutes of server usage by
    # end user in a day.
    total_use_time= 0.0

    #Iterate through the "Server" dictionary's key and value items
    #using a for loop.
    for key,value in server.items():

        #For each end user key, add the asociated time value to the
        #total sum  of all end user use time.
        total_use_time += server[key]
        
    # Round the returned value and limit to 2 decimal places
    return round(total_use_time, 2)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(sum_server_use_time(FileServer))
print(" ")
print("Dictionaries skills 2")
# This function receives a dictionary, which contains common employee 
# last names as keys, and a list of employee first names as values. 
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the 
# values ["Maria", "Hugo", "Lucia"] should be converted to a list 
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].
def list_of_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.
    full_names=[]
    # The outer for loop iterates through each "last_name" key and 
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():
        # The inner for loop iterates over each "first_name" value in 
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:
            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name".
            full_names.append(first_name+" "+last_name)
    # Return the new "full_names" list once the outer for loop has 
    # completed all iterations.
    return (full_names)

print(list_of_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
print(" ")
print("-----Dictionaries Skills 3")
# This function receives a dictionary, which contains resource 
# categories (keys) with a list of available resources (values) for a 
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which 
# categories (values) each resource (key) belongs to. 
def invert_resource_dict(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type using
    # empty {} curly brackets.
    new_dictionary ={}
    # The outer for loop iterates through each "resource_group" and 
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in 
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has 
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            #if false (else), then add the resource as a new key with the
            # resourse_group as a value for that key
            else:
                new_dictionary[resource]=[resource_group]
    # Return the new dictionary once the outer for loop has completed  
    # all iterations.
    return(new_dictionary)
print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"], "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))  
######Practice quiz: Dictionaries
print("###########Practice Quiz Dictionaries")

print('exercise 1:')
def email_list(domains):
    emails = []
    for domain_name, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user,domain_name))
        return(emails)
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
print('Exercise 2:')
def groups_per_user(group_dictionary):
    user_groups={}
    for group_name,users in group_dictionary.items():
        for user in users:
            if user in user_groups:
                user_groups[user].append(group_name)
            else:
                user_groups[user]=[group_name]
    return (user_groups)
print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))    
print("Exercise 3:")
def add_prices(basket):
    total=0
    for item,price in basket.items():
        total += price
    return round(total, 2)
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
####Object oriented programming 
print("################ Object-oriented programming")
class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"
honeycrisp = Apple()
print(honeycrisp.color)
#Modify variables
print("---modifying the variables on class")
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)
honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)
#Other special methods
print(honeycrisp)
