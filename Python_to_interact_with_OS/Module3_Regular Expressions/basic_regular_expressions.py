import re
result = re.search(r"aza", "plaza") #<re.Match object; span=(2, 5), match='aza'>
print(result)
result = re.search(r"aza", "bazaar") #<re.Match object; span=(1, 4), match='aza'>
print(result)
result = re.search(r"aza", "maze") #None
print(result)
print(re.search(r"^x", "xenon")) #<re.Match object; span=(0, 1), match='x'>
print(re.search(r"p.ng", "penguin")) #<re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "clapping")) #<re.Match object; span=(4, 8), match='ping'>
print(re.search(r"p.ng", "sponge")) #<re.Match object; span=(1, 5), match='pong'>
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) #<re.Match object; span=(0, 4), match='Pang'>