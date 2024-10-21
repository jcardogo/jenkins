#.* repeated as many times as possible incluiding 0
import re
print(re.search(r"Py.*n", "Pygmalion")) #.* represent any combination of characters or number until the character "n"
print(re.search(r"Py.*n", "Python Programming")) # in this case it is returning the whole string becouse it is taking as many characters as it is possible to so avoid this use next line 
print(re.search(r"Py[a-z]*n", "Python Programming")) # the use of a class [a-z] means that until it finds ona "n" and a space separating words it would export just the forst word starting with Py and all character in it 
print(re.search(r"Py[a-z]*n", "Pyn"))
#use of + and ? as repetition qualifiers that allow us to create more complex expressions
print(re.search(r"o+l+", "goldfish")) # "+" character matches one or more ocurrencies of the character that comes before him here we can see one match of each character 
print(re.search(r"o+l+", "woolly")) # here we can see two matches of each character
print(re.search(r"o+l+", "boil")) #as this is a looking for "ol" it show None as response becouse we have a "oil" that contains one "i" character interfiering our patern
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
#Exercise: The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 
import re
def repeating_letter_a(text):
  result = re.search(r"[aA]+", text)
  print(result)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
