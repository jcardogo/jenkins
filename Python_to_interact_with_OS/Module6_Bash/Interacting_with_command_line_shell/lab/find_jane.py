import re

string="holajanehola"
print(string)
pattern=r"jane"
replacement="joeb"
updated=re.sub(pattern, replacement, string)
print(updated)