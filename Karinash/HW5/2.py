n = int(input("Enter a number (n) to print Fibonacci numbers up to: "))
a, b = 0, 1
fibonacci_sequence = [a]

while b <= n:
    fibonacci_sequence.append(b)
    a, b = b, a + b

print(f"Fibonacci numbers up to {n}: {fibonacci_sequence}")

