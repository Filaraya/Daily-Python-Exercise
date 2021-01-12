"""
Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
"""

enter_number = int(input("Please enter any integer: "))
result= enter_number % 2

if result == 0:
    print("the number is Even")
else:
    print("the number is Odd")
    
