#cat hello.py
#!/usr/bin/env python3

name = input("Please enter your name: ")
print("Hello, " + name)
'''
./hello.py 
Please enter your name: Roger
#Output will be Hello, Roger
'''
def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")
    
print("Goodbye!")
'''
./seconds.py 
Welcome to this time converter
Enter the number of hours: 1
Enter the number of minutes: 2
Enter the number of seconds: 3

Do you want to do another conversion? [y to continue] y
Enter the number of hours: 3
Enter the number of minutes: 2
Enter the number of seconds: 1

Do you want to do another conversion? [y to continue] n
'''
######Standard Streams ------ Input and Output streams
# standard input : STDIN
# standard output : STDOUT
# standard error : STDERR
'''
cat streams.py
'''
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)

'''
./streams.py 
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z
'''
'''
cat streams.py
'''
#different input
'''
./streams.py 
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z
'''

######Environmental Variables
#Shell  is a command base interface used to interact with the operative system
'''
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cat variables.py
'''

#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

'''
./variables.py 
export FRUIT=Pineapple
./variables.py 
'''

#########Command line arguments and exit status
'''
cat parameters.py 
'''
#!/usr/bin/env python3
import sys #all incluided arguments are located on sys module
print(sys.argv) #this code create a list with all the parameters added on the code when executing the script

'''
./parameters.py
['./parameters.py'] 

./parameters.py one two three
['./parameters.py', 'one', 'two', 'three']


wc variables.py
7 19 174 variables.py 	
echo $?
0

wc notpresent.sh
wc: notpresent.sh: No such file or directory
echo $?
1
'''

#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

'''
./create_file.py example
echo $?
0

cat example 
New file created
./create_file.py example
Error, the file example already exists!
echo $?
1
'''

