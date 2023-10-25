def fi(n):
    if n == 1 or n == 2: return 1
    return fi(n-1) + fi(n-2)

num = int(input('Enter the number: '))



print(f'{num} = {fi(num)}')
