"""an immutable list is called a tuple.
A tuple looks just like a list except
you use parentheses instead of square brackets."""

# we can ensure that its size doesn’t change by putting the dimensions into a tuple
rec_dimensions = (90, 20)
print("all tuple: ",rec_dimensions,"\n"+ "first tuple: ",rec_dimensions[0])

#rec_dimensions[1]=30 #resulst error since tuples is immutable

rec_dimensions = (30, 40)
for rec_dimension in rec_dimensions:
    print (rec_dimension)
    