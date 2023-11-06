n = int(input("Enter number:"))
m = 1
while n > 1:
    m *= n
    n -= 1
print( "The factorial of this number is equal {0}".format(m))