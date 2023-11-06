n = int(input('Enter number '))
factorial_n = 1
for i in range(1, n + 1):
    factorial_n *= i

print(f'Factorial number {n} = {factorial_n}')
