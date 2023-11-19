def return_largestNumber(num1, num2):
    """This function returns the largest number of two numbers."""
    if num1 > num2:
        return num1 
    elif num1 == num2:
        return f"{num1} is equal to {num2}"
    else:
        return num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = return_largestNumber(num1, num2)
print(result)
print(return_largestNumber.__doc__)




