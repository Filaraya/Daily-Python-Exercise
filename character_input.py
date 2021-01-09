"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
import datetime

name = input ("What is your name: ")
age = int(input("How old are you now? "))
now = datetime.datetime.now()
by_year= int((now.year + 100) - age)
print (name + ", you will be 100 years old by ", by_year)
