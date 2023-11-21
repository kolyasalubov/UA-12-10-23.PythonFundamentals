n = int(input('Enter n '))
list_Fibonacci = [0, 1]
for i in range(1, n - 1):
    list_Fibonacci.append(list_Fibonacci[i - 1] + list_Fibonacci[i])

print('Sequence of Fibonacci numbers: ', *list_Fibonacci)
