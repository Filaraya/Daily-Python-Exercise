    
#parrot - repeat the word
prompt = "\n I will repeat the word you write"
prompt += "\n if need to quit write 'quit'."

message = "test"
while message != 'quit':
    message = input(prompt)
    print(f"\t{message}")
    print("")
print("Thank you! Done!!")
