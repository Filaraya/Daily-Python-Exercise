cities =['paris','asmara','toronto','tokyo']
other_city = 'kartum'
your_city = 'kampala'
#to check and convert city
for city in cities:
    if city =='asmara':
        print (city.upper())
    else:
        print(city.title())
#to check if other city in the list of cities
if other_city in cities:
    print ("the city is in the list")
else:
    print ("the city is not in the list")
#to check if your city is not in the cities list
if your_city not in cities:
    print("your city is not in the list")
else:
    print("your city is in the list")
#Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

#stage of life
age = 17
if age < 2:
    print("the person is a baby")
elif age < 4:
    print("the person is a toddler")
elif age < 13:
    print ("the person is a kid")
elif age < 20:
    print ("the person is a teenager")
elif age < 65:
    print("the person is an adult")
else:
    print ("the person is an elder")

#favorite fruit
favorite_fruits =['banana','orange','apple','avocado']
for i in favorite_fruits:
    if i=='banana':
        print('you like banana')
    elif i=='orange':
        print('you like orange')
    elif i=='apple':
        print('you like apple')
    elif i== 'avocado':
        print('you like avocado')
    else:
        print('the fruit is not your favorite fruits')
print('process DONE!')