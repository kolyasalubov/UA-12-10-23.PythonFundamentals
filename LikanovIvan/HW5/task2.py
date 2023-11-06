n = int(input('Enter how many Fibonacci numbers you need (begin from 2):\t'))
list_Fib = [0,1]
for i in range(1, n - 1):
    list_Fib.append(list_Fib[i - 1] + list_Fib[i])

print('Your Fibonacci numbers: ', *list_Fib)