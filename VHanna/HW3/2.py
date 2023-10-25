#add number
a = input('Your four-digit natural number:')

#1 the product of the digits of this number
#I split the entered number into 4 separate numbers and convert them into a numeric format
one = int(a[0])
two = int(a[1])
tree = int(a[2])
four = int(a[3])

#I calculate the product of the four obtained numbers
product = one*two*tree*four

print(f'The product of the digits of {a}:',product)

#write a number in revers order
b = a[::-1]
print(f'Number {a} in revers order:', b)

#in ascending order sort the numbers included in the given number
print(f'Number {a} in ascending order:', sorted(a))