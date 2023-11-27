def calculate_factorial(n):
    factorial_result = 1

    for i in range(1, n + 1):
        factorial_result *= i

    return factorial_result

number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    factorial_result = calculate_factorial(number)
    print(f"The factorial of {number} is {factorial_result}")