def calculate_factorial(n):
    factorial = 1
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial


num = int(input("Enter a number to calculate its factorial: \t"))

result = calculate_factorial(num)
print(f"The factorial of {num} is: {result}")