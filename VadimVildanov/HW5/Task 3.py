number = int(input("Enter your factorial: "))
fact = 1
for i in range(2, number + 1):
    fact = fact * i
print("The factorial of ", number, " is: ", fact)
