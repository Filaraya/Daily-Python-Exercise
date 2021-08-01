#using break in while loop
prompt = "Enter the city you want to go."
prompt += "\n if need to quit, write 'quit'."

while True:
    message = input(prompt)
    #print (message)
    
    if message == 'quit':
        break
    else:
        print ("I'd love to go: ", message)
print ("Thank you, DONE!!")

