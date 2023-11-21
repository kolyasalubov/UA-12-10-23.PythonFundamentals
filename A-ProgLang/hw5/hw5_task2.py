n = int(input("Enter number n: "))

fibonacci = [0, 1]

while fibonacci[-1] + fibonacci[-2] <= n:
    next_fibonacci_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci_number)
print("Fibonacci numbers to", n, ":", fibonacci)