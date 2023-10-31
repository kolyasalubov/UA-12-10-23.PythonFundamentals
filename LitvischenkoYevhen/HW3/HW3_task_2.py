num = input("Enter four-digit natural number:")
num_int = list(map(int, list(num)))
prod = 1
for i in num_int:
    prod *= i 
print(f'Product of the digits of number : {prod}')
num = str(num)[::-1]
print(f'Revers product of the digits : {num}')
num_int.sort()
print(f'Sort digit in number : {num_int}')