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



