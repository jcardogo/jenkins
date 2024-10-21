import re
print(re.search(r".com", "welcome")) #this code would use . as a special character, so it wont fetch ".com" instead ot will fetch "com"
print(re.search(r"\.com", "welcome")) #using special character "\" it would include special character "." into the search as ".com"
print(re.search(r"\.com", "mydomain.com")) #this is a good example of working ".com search"
print(re.search(r"\w*", "This is an example")) #"\w" matches letters, number, spaces and underscores of the first word
print(re.search(r"\w*", "And_this_is_another"))
#\d for matching digits
#\s for matching white space characters as space, tab or newline
#\b for word boundaries


###Exercise: Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
import re
def check_character_groups(text):
  result = re.search(r"\w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

#www.regex101.com