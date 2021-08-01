#using continue in while
##the continue statement tells Python to ignore the rest of the loop
##and return to the beginning. 

current_number = 0
while current_number <=10:
    current_number += 1
    
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
    
print("DONE!!")