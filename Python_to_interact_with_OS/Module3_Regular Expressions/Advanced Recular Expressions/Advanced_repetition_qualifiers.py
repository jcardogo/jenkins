import re
print(re.search(r"[a-zA-Z]{5}", "a ghost")) # to identify a string containing 5 letters 
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # in this case it finds more matches but is only showing the first "scary"
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # in this case it will show all matches but includes also one match that is actually longer than 5 characters
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) #adding "\b" we define the begining and end of the matching string so it will show only the words containing 5 characters
print(re.findall(r"\w{5,10}", "I really like strawberries")) #we can also add ranges to the matching pattern and in this case the range of characters is betwen 5 and 10 characters but it cut the word loger than 10
print(re.findall(r"\w{5,}", "I really like strawberries")) #this code will pirint every word that contains more than 5 characters
print(re.search(r"s\w{,20}", "I really like strawberries")) #this code matches any word starting with "s" and containing up to 20 characters