#write a function called make_shirt()
def make_shirt(size,message):
    """T-shirt displays its size and message on it"""
    print(f"\nThe size of the T-Shirt is: {size}")
    print(f"message on it: {message}")
#call make_shirt function    
make_shirt("38'","Fight Cancer")
make_shirt("43'","Be Good!")

#function that accepts name of the city and its country
def describe_city(city,country):
    """describe a city and its country"""
    print(f"\n{city} is in {country}")

#call describe_city function
describe_city('Asmara','Eritrea')
describe_city('Roma','Italy')

#using return values in the function
def get_formatted_name(first_name,last_name,middle_name=''):
    """Return a full name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
#call the get_formatted_name function
teacher = get_formatted_name('david','john','sam')
actor = get_formatted_name('calieb','joseph')
print(teacher)
print(actor)