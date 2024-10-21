#Capturing Groups: Portions of the pattern that are enclosed in parentheses 
import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada") 
print(result)
print(result.groups()) # this code returns a tuple stracted from the result
print(result[0]) #elements of the tupple are accesible in this case element 0 is whole string 
print(result[1]) #after element 0 the tupple "result" will bring each element on the tupple an we can reach each element to use it on further functions
print(result[2])
print("{} {}".format(result[2],result[1])) 
def rearrange_name (name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name) #this code will capture a group with two elements one before the comma and one after the comma 
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Alejandro, Cardoso"))
print(rearrange_name("Martina, Cardoso"))
print(rearrange_name("Juli, Cruz .T"))

