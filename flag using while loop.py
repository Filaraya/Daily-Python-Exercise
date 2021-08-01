#using Flag with while loop and if
prompt = "\n Enter a word, I will repeat"
prompt += "\n if need to quit write 'quit'."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print("\t",message)
print("Thank you! DONE!!")
        