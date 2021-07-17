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
    