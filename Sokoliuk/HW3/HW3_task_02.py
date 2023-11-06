while True:
    number = input("Enter your 4-digit number: ")
    if number.isdigit():      
        if len(number) > 4 :
            print("Wrong! Only 4-digits number. The CPU power isn't allow you to compute more! ")
        else:
            break
    else:
        print("Wrong! Only digits allowed! ")

product = 1
for digit in number:
    product *= int(digit)

print(f"The product of digits in your number: {product}")

print(f"Your number in reverse order: {number[::-1]}")

print(f"The digits of your number in ascending order: {''.join(sorted(number))}")