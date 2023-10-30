number = 7896
digit = number
product = 1

while digit > 0:
    product = product * (digit % 10)
    digit = int(digit / 10)

reversed_number = int(str(number)[::-1])

print(f"Product of all digits in {number} is {product}")
print(f"Reversed number is: {str(reversed_number)}")
print(f"Sorted list od digits the included in the {number}: {sorted(str(number))}")