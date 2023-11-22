# Create a list of integer elements
integer_list = [1, 2, 3, 4, 5]

# Use a loop to change the type of elements to float
float_list = [float(num) for num in integer_list]

# Print the resulting float list
print(float_list)

# Prompt the user to enter a number 'n'
n = int(input("Enter a number (n) to print Fibonacci numbers up to n: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the first Fibonacci number (0)
print(a)

# Print Fibonacci numbers up to 'n'
while b <= n:
    print(b)
    a, b = b, a + b


# Prompt the user to enter a number
j = int(input("Enter a number to calculate its factorial: "))

# Initialize the result to 1
result = 1

# Calculate the factorial of the entered number
for i in range(1, j + 1):
    result *= i

# Print the factorial result
print(f"{j}! = {result}")
