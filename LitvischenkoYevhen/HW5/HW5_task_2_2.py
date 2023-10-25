num = int(input('Enter the number: '))
a, b = 0, 1
for i in range(num):
    a, b = b, a + b
print(f'{num} = {a}')