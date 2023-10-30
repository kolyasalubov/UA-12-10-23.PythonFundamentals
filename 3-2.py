number = int(input("Enter 4 digit natural number: "))

product = 1
for digit in str(number):
    product *= int(digit)

reversed_number = int(str(number)[::-1])

sorted_digit = '' .join(sorted(str(number)))

print(f"product:{product}")
print(f"reverse:{reversed_number}")
print(f"sorted:{sorted_digit}")