""" Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live .
You should have keys such as first_name, last_name, age, and city .
Print each piece of information stored in your dictionary ."""

person = {
    'first_name':'David',
    'last_name':'Jhon',
    'age':72,
    'city':'Las Vegas'
    }
print ("the dictionary of person: ",person)
print (f"the age of {person['first_name']} is {person['age']} old.")

for key,value in person.items():# to loop all items in the dictionaries
    print('key:',key)
    print('value:',value)
    print('')
    
for key in person.keys():#only to print keys of the keys
    print('only the key: ',key)
    
for value in person.values():#to print only values of the dictionaries
    print('only the value: ',value)

#persons dictionaries with thier countries
persons = {
    'Hanna':'USA',
    'Anita':'India',
    'Sami':' Egypt',
    'Pedro':'Italy'
    }
print("persons with the countries: ",persons)

for name,country in persons.items():
    print (f"Hi {name}, I think you are from {country}.")
    
guests = ['Abdu','Phil','Anita']
for guest in guests: #check if guest is in the dictionary.
    if guest in persons.keys():
        print(f"Hi {guest}, thank for submiting")
        
    else:
        print(f"Hi {guest}, please fill the form.")

#list in dictionary
#store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','cheese']
    }
#to print the whole information
print(f"you have ordered {pizza['crust']}")
for topping in pizza['toppings']:
    print ("\t:"+topping)
    
#morethan one items in the list of dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(f"{name}'s favorite_language are:")
    for language in languages:
        print(f"\t{language}")
#many users
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username,userinfo in users.items():
    print("\nUsername: " + username)
    full_name = userinfo['first'] + " " + userinfo['last']
    location = userinfo['location']
    print("\tfull_name: " + full_name.title())
    print("\tlocation: " + location.title())