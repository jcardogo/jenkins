import re
def check_time(text):
  pattern = r"^(0?[0-9]|1[0-2]):([0-5][0-9])\s?(AM|PM|am|pm)$|^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False