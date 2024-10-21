#using index
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6]) #this method migth have an issue on the number of digits on the process ID 

#using regex
import re
regex = r"\[(\d+)\]" #This regular expression matches a string enclosed in square brackets followed by one or more digits. Then, it uses the re.search() function to search the string log for a match to the regular expression.
result = re.search(regex, log)
print(result[1])
