#if check a number is even or odd
number = input("Enter a number to check even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")

#count number
current_number = 1
while current_number <=5:
    print(current_number)
    current_number +=1
    
#parrot - repeat the word
prompt = "\n I will repeat the word you write"
prompt += "\n if need to quit write 'quit'."

message = "test"
while message != 'quit':
    message = input(prompt)
    print(f"\t{message}")
    print("")
print("Thank you! Done!!")

