"""
Movie Tickets: A movie theater charges different ticket prices depending on a person’s age .
If a person is under the age of 5, the ticket is free;
if they are between 5 and 10, the ticket is $25;
and if they are over age 10, the ticket is $50 .
Write a loop in which you ask users their age,
and then tell them the cost of their movie ticket .
"""
prompt = "Enter the age of the person: "
prompt += "\nto quit enter 'quit'. "


while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 5:
        print ("The price of ticket is Free")
        
    elif age < 10:
        print ("The price of the Ticket is $25")
    
    elif age > 10:
        print ("The price of the Ticket is $50")
        
    else:
        print ("Please enter the correct age")
print("DONE")