#Write a Python program to print the calendar of a given month and year.

import calendar #import calendar module 
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
