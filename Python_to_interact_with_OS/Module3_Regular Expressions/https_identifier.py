'''
You have a list of website urls that includes both securely encrypted websites that begin with https://www. and the unencrypted websites that begin with http://. The list includes websites that end in .com and .co. 

Complete the secure_website_domain() function so it returns the part of the website between www. and the last part of the url (.com or .co) for only the secure websites. 
'''
import re
def secure_website_domain(website):
 pattern = r'[htps://]{8}\w*.(\w*).\w*' # enter the regex pattern here
 result = re.search(pattern, website) # enter the re method here
 if result is None:
  return ""
 return result.groups()# enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text