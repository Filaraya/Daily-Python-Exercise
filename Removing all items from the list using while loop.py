#Removing All Instances of Specific Values from a List
#if the item repeated several times use while loop

fruits = ['banana', 'avocado','apple','avocado','grape']
print(fruits)
while 'avocado' in fruits:
    fruits.remove('avocado')
print(f"the rest of the fruits are: {fruits}")