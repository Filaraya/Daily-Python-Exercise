"""
Enter the numbers of intiger to evaluate, and return
the how many are evens and how many odds.
"""
numbers =  int(input("Enter the numbers to evaluate: "))
intigers = []
odd_int = []
even_int = []
for i in range(numbers):
    num = int(input("Enter any intiger: "))
    intigers.append(num)
for intiger in intigers:
    if intiger % 2 == 0:
        even_int.append(intiger)
    else:
        odd_int.append(intiger)
print(f"You entered {numbers}'s")
even_count = len(even_int)
odd_count = len(odd_int)
print(f"You entered {even_count}, even numbers")
print(f"You entered {odd_count}, odd numbers")