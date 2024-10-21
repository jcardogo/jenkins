import re
#
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia")) #this code esctirctly call the words starting with "A" and ending with "a"

#
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$" # in this code we incluided any starting "^" character uper or lower case leters or undescore and also ends "$" with any leter or number incluiding also underscore  
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable")) #this is not a valid variable name becouse includes black spaces
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1")) #this is not a valid variable becouse it includes a number at the beggining


#Exercise: Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-zA-Z\ ]+[.?!]$", text) 
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

#r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.
#r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.
#r”^(.+)\/([^\/]+)\/” This line of code matches any path and filename.

#https://docs.python.org/3/howto/regex.html
#https://docs.python.org/3/library/re.html
#https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
