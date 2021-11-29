"""
You are given some input, and you are required to check
whether they are valid mobile numbers.
A valid mobile number is a ten digit number
starting with a 7,8 or 9.
"""

import re

N = int(input("Enter the number of phone numbers to validate: "))

for i in range(N): # N the digit of phone number
    phone = input("Enter phone number: ")
    if(len(phone)==10 and phone.isdigit()):
        output = re.findall(r"^[789]\d{9}$",phone)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
