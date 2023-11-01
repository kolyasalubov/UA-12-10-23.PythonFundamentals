four_digit_number = input("Enter a four digit number: ")
l1 = list(four_digit_number)
product = eval(l1[0]) * eval(l1[1]) * eval(l1[2]) * eval(l1[3])
str_product = str(product)
l2 = list(str_product)
print(f"The product of 4-difit number >> {l1[0]} * {l1[1]} * {l1[2]} * {l1[3]} = {product}")
print(f"Reversed order for 4-digit number >> {l1[::-1]}")
print(f"Reversed order for result of product >> {list(reversed(l2))}")
print(f"Sorted 4-digit number in ascending order >> {list(sorted(four_digit_number))}")



