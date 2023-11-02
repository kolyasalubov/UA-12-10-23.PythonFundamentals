num=input('Enter 4-digit natural number:')

first=int(num[0])
second=int(num[1])
third=int(num[2])
fourth=int(num[3])

product=first*second*third*fourth

print('Product:',product)

reverse=num[::-1]
print('In reverse order:', reverse)

sorted=sorted(num)
print('in ascending order:', sorted)

