print('Number division 2: ', *[i for i in range(2, 11, 2)])
print('Odd number divisibl by 3: ', *[i for i in range(3, 11, 3) if i % 2 == 1])
print('Not divisible 2 or 3: ', *[i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0])
