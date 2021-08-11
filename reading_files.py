"""
read file
"""
#to read a file 
with open("pi_digits.txt") as file_object:
    content = file_object.read()
print(content.rstrip())

#to read line by line
print("Reading line by line")
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

#making a list of lines from a File
with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
    print(lines) #read the second line
    print(lines[1])