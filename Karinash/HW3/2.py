number = int(input("Enter a four-digit natural number: "))

if 1000 <= number <= 9999:
    digit_1 = number // 1000
    digit_2 = (number // 100) % 10
    digit_3 = (number // 10) % 10
    digit_4 = number % 10
    product_of_digits = digit_1 * digit_2 * digit_3 * digit_4

    reversed_number = int(str(number)[::-1])

    sorted_digits = sorted([digit_1, digit_2, digit_3, digit_4])
    sorted_number = sorted_digits[0] * 1000 + sorted_digits[1] * 100 + sorted_digits[2] * 10 + sorted_digits[3]

    print(f"Product of the digits: {product_of_digits}")
    print(f"Number in reverse order: {reversed_number}")
    print(f"Number with digits in ascending order: {sorted_number}")
else:
    print("Please enter a valid four-digit natural number.")
    
