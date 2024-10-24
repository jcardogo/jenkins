'''
You are reading an article that includes some government websites in the form:

 https://www.website-domain.gov 

You’d like to make a list of these websites by extracting them from the text automatically, 
instead of copying and pasting them by hand. Complete the function find_gov_urls() to accomplish 
this task for all websites that end with .gov.
'''
import re
def find_gov_urls(website):
 pattern = r'https?://[a-zA-Z0-9.-]+\.gov' #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []