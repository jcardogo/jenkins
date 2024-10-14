with open("sample_data/declaration.txt", "rt") as textfile: #this function includes two arguments: the file path and the mode ("r" means open for reading only, and "t" tells Python to expect a text file)
    for line in textfile:
        print(line)
f= open ("sample_data/declaration.txt", "w") #THe code tells Python to open this for writing ("w" mode)
#“r”  open for reading (default)
#“w”  open for writing, truncating the file first
#“x”  open for exclusive creation, failing if the file already exists
#“a”  open for writing, appending to the end of the file if it exists
#“+”  open for both reading and writing
f= open('workfile', 'w', encoding="utf-8") #in this example the encoding='utf-8' specifies that the file should be opened with UTF-8, the modern de facto standard.
