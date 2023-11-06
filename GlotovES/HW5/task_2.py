def print_fibon(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter a number (n) to print Fibonacci numbers up to: "))
print(f"Fibonacci numbers up to {n} :")
print_fibon(n)
