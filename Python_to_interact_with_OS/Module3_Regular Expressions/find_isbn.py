'''
International Standard Book Numbers (ISBNs) are used to uniquely identify published books. They follow a 13-digit format: 

3XXX-X-XX-XXXXXX-X

where each X represents one numeric digit. You have a list of books, information about those books, and their ISBN numbers. 
You want to extract the 6 digits of the ISBN that come before the last hyphen of each book’s ISBN number. However, you need 
to be careful to avoid 6-digit strings that are not part of the ISBN numbers you’re interested in. 

Complete the find_isbn() function so you can use it to extract the 6-digit portion of the ISBN numbers of the books on your list. 
'''
import re 
def find_isbn(list):
  pattern = r"\b\d{3}-\d{1}-\d{2}-(\d{6})-\d{1}\b" #enter the regex pattern here
  result = re.search(pattern, list) #enter the re method  here
  if result is None:
    return ""
  return "{}".format(result[1]) #return the correct capturing group


print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank