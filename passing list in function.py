#passing a list in function
def greet_users (names):
    """greet to users"""
    for name in names:
        msg = "Hello " + name.title() + ", nice to meet you"
        print(msg)
#to apply the function
usernames = ['David','John','sara']
greet_users(usernames)

#creat a list
def create_names(listNames):
    """create a list of users"""
    #listNames = []
    while True:
        print("\nCreate list of names")
        print("to quit enter 'q'.")
        fName = input("What is your name, please: ")
        if fName == 'q':
            break
        else:
            listNames.append(fName)
    print(listNames)
#to call a function
listNames = []
create_names(listNames)
greet_users(listNames)