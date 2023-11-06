num = int(input("Enter a number to calculate its factorial: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")

