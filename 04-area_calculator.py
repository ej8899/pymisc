x = input("what is side one of rectangle? ")
y = input("what is side two of rectangle? ")

print("the area of rectangle is: ");

# unlike JS, python won't convert or assume types so below is an error
# print (x * y)

# below 'works', but it puts the two strings together
print (x+y)

# below is proper output:

z = int(x) * int(y)
print (f"Area is: {z}")
