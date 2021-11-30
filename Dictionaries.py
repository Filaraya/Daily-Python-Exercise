""" Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live .
You should have keys such as first_name, last_name, age, and city .
Print each piece of information stored in your dictionary ."""

#person dictionary
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
    'Einstein': {
        'first': 'Albert',
        'last': 'Einstein',
        'location': 'princeton',
        },
    'Mcurie': {
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
    
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'John',
    'owner': 'Guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)
pet = {
    'animal type': 'chicken',
    'name': 'Clarence',
    'owner': 'Tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Peso',
    'owner': 'Eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)
print(pets)

# Display information about each pet.
for pet in pets:
    print(f"the pet owner is: {pet['name'].title()}")
    for key, value in pet.items():
        #print(f"animal type: {key['animal type'].title()}")
        #print(f"owner: {key['owner'].titel()}")
        print(f"\t{key} : {value}")


#favorite places
favorite_places = {'John':'Cairo','David':'Tokyo','Susan':'Las Vegas'}
for name, city in favorite_places.items():
    print(f"{name},your favorite city is {city}")

#cities information
cities = {
    'Jakarta':{
        'country':'indonsia',
        'population':'30M',
        'fact':'cool area',
        },
    'Roma': {
        'country':'Italy',
        'population':'3M',
        'fact':'old city',
        },
    'Cairo':{
        'country':'Egypy',
        'population':'100M',
        'fact':'Pyramid',
        }
    }
print(cities)
for city,info in cities.items():
    print (f"the information about {city} are: ")
    print(f"\t country of the city: {info['country']}")
    print(f"\t population of the city: {info['population']}")
    print(f"\t fact of the city: {info['fact']}")
    print("")
    
