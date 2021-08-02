#Filling a Dictionary with User Input
responses = {}
polling_active = True
while polling_active:
    #prompt user to input 
    name = input("what is your name, please: ")
    response = input("which city you are from? ")
    #to store the data
    responses[name]=response
    #ask the user to repeat
    repeat = input("\n would like to repeat? (yes/no) ")
    #check if the poll to repeat
    if repeat == 'yes':
        polling_active = True
    else:
        polling_active = False
#display the result
print("\n- - - Poll Result - - -")
for name,response in responses.items():
    print(f"{name},you are from {response} city")
