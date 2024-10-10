####Reading files
file=open("spider.txt") #OPen the file "sipider.txt" and asing a file object to the variable file
print(file.readline()) #as it is the first time it reads the first line of a file object
print(file.readline()) #as second time it is reading second line of the file 
print(file.read()) #print all the remaining lines of the file object
file.close() #Is very important to close the file on open-file-close approach 
with open("spider.txt") as file: #It is a way how you can use a file object without having to clos it 
    print(file.readline())
with open("spider.txt") as file: 
    for line in file:
        print(line.upper()) #result show that after every line the open method add a "/n" character and it result on a extra line added after each line
with open("spider.txt") as file: 
    for line in file:
        print(line.strip().upper()) #avoiding to show the added "/n" after each lie we use the strip method to remove it 
file =open("spider.txt") #creating file variable objet from opening file
lines=file.readlines() #creating a variable lines as a list to alocate all lines on file
file.close() #closing "spidet.txt" file to avoid blocking other to use it
lines.sort() #using lines list to sort the lines on it 
print(lines) #printing sorted list of lines 
#####Writing files 
with open("novel.txt", "w") as file: #opening file in writing only mode "w" 
    file.write("It was a dark and stormy night")


