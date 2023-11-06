def factorial(n):
    fes = 1
    for i in range (1, n+1):
        fes *= i
    return fes
for i in range(1, 10):
    print(i, "!=", factorial(i), sep =" ")

    