
from faker import Faker
fake = Faker()

fruits = ['banana', 'orange', 'apple', 'avocado']
print("list of fruits", fruits)
first_fruits = fruits[0]
print("formatted list of fruits: ", first_fruits)

# list of fruits
print("list of fruits: ", fruits)

# list of fruits in format way
print(*fruits, sep="\n")

# to add to the list in the last
fruits.append('lemon')
print(fruits)

print("lemon added to the end :", fruits)

"""Guest List: If you could invite anyone, living or deceased, to dinner,
who would you invite? Make a list that includes at least three people you’d like
to invite to dinner . Then use your list to print a message to each person,
inviting them to dinner ."""

guests = [fake.name(),fake.name(),fake.name()]
print (guests)

message = f'hello, {guests[0].title()}'
print (message)
print(len(guests))

"""Add a print statement at the end of your program
stating the name of the guest who can’t make it ."""

print ("person cann't make it: ", guests[1])

"""Modify your list, replacing the name of the guest
who can’t make it with the name of the new person you are inviting ."""

new_guest = f'{fake.name()}'
guests[1]= new_guest

print (guests)
print(len(guests))

"""Print a second set of invitation messages,
one for each person who is still in your list ."""

print (guests)

"Use insert() to add one new guest to the beginning of your list ."
guests.insert(0,'Eric')
print (guests)
print (len(guests))

"Use insert() to add one new guest to the middle of your list ."
length = len(guests)
value_middle = (length//2)
print (value_middle)
guests.insert(value_middle, 'Asmara')
print (guests)
print (len(guests))

"Use append() to add one new guest to the end of your list."
appendded_name = f'{fake.name()}'
guests.append(f'{appendded_name}')
print ("appended: ",guests)

#Shrinking Guest List
temp_removed = guests.pop(4)
print (guests)
print (temp_removed)
print (len(guests))
print (len(guests))

"to delete from the list"
del guests[3]
print (guests)
print (len(guests))

"to remove from list by value"
guests.remove('Asmara')
print (guests)
print (len(guests))

#orginizing list
countries = [fake.country(),fake.country(),fake.country()]
print ('unsorted: ' ,countries)
print ('temporary sort: ',sorted(countries)) #temporarly sort
countries.sort () #to sort premanently
print ('sorted alphabetical: ',countries)
countries.sort(reverse = True) #to sort reverse
print ('the reverse sorted countries: ',countries)
countries.reverse()
print ('reverse used: ',countries) #permanently reversed by reverse methods
