number = 1233  
product_of_digits = 1
for digit in str(number):
    product_of_digits *= int(digit)

reverse_number = int(str(number)[::-1])
sorted_digits = int(''.join(sorted(str(number))))

print(f"Product of the digits: {product_of_digits}")
print(f"Number in reverse order: {reverse_number}")
print(f"Digits sorted in ascending order: {sorted_digits}")