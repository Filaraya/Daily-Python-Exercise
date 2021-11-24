"""
Print the list of integers from 1 through n
as a string, without spaces.
"""
n = int(input("Enter a n value: ")) #enter the number 
values='' 
for value in range(1,n+1):
    value = str(value)
    values += value
print(values)
