fibonacci_numbers = int(input("entered number n: "))

a, b = 0, 1

print("Fibonacci numbers:")
while a <= fibonacci_numbers:
    print(a)
    a, b = b, a + b
