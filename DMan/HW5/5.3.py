# honestly found it on the internet:

# import math
# n = int(input("Enter a number to calculate its factorial"))
# print(math.factorial(n))


num = int(input("Enter a number to calculate its factorial"))

factorial = 1
while num > 1:
    factorial *= num
    num -= 1
 
print("The factorial", factorial)
