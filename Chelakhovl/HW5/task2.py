n = int(input("Enter a number (n): "))

f1, f2 = 0, 1

while f1 <= n:
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2


