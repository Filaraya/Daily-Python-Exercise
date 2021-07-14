#looping through an entire list
from faker import Faker
fake= Faker()
# students = [fake.name(), fake.name(), fake.name()]
# 
# print (">>show the all the list")
# print (students)
# print (">>show all the list out of the list")
# print (students[0],students[1],students[2], sep = "\n") # the same as for loop
# print (">>the list using the for loop")
# for student in students:
#     print(student)
# 
# print(">>telling students")
# for student in students:
#     print (student,", You are amazing student!") #adding sentence
#     print ("In the last semester", student+ "you did great\n")
# print ("Conguratulation to all!")

#making numerical lists
"to print a list of numbers using range"
squares= []
for value in range(1,11):
    square = value**2
    squares.append(square)
print (squares)

#Simple Statistics with a List of Numbers
print ("The min of list: ", min(squares))
print ("The max of list: ", max(squares))
print ("The sum of list: ", sum(squares))

#Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .
cubes = [value**3 for value in range (1,11)]
print("The list of Cubes: ", cubes)

names = []
for name in range(1,10):
    name = fake.name()
    print(name)
    names.append(name)
print (names)

first_three = []
for name in names [:3]: #slicing the first three elements
    first_three.append(name)
print ("\n the first three names: ",first_three)

last_three =[]
for name in names [-3:]: #slicing the first three elements
    last_three.append (name)
last_three.reverse()
print ("\n the first last three names: ",last_three)

just_last =[]
for name in names [::-1]:
    just_last.append(name)
print ("\n the last three list without reversed: ",just_last[:3])

guest_names = names[:] #copying all the list and make new list
print("\nnew list of names: ",guest_names)
