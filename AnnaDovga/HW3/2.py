four_digit = input()

#product of the digits

product_digit = 1
for i in four_digit:
    product_digit *= int(i)
print(product_digit)

#number in reverse order

print(four_digit[::-1])

#sort the numbers

sorted_digit = ''
while len(four_digit) > 0:
    sorted_digit += min(four_digit)
    index_min = four_digit.find(min(four_digit))
    four_digit = four_digit[:index_min] + four_digit[index_min+1:]
print(sorted_digit)
