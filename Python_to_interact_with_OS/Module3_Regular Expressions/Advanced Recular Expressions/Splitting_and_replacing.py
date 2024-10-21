import re
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!")) #use any regular expression to split a sentence, in this case we mentioned ".", "?", and "!"
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")) #replacing part of the string depending on ur selected regular expression
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")) #this code replace our regular expression matched with a regular expression to use each element of it to give them specific order

