def fibonacci_up_to_n(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

max_number = int(input("Enter the maximum number: "))
fibonacci_up_to_n(max_number)