number = int(input("Input a four-digit natural number: "))

if 1000 <= number <= 9999:
    digit_1 = number // 1000
    digit_2 = (number // 100) % 10
    digit_3 = (number // 10) % 10
    digit_4 = number % 10

    product = digit_1 * digit_2 * digit_3 * digit_4

    reversed_number = int(str(number)[::-1])

    sorted_number = int(''.join(sorted(str(number))))

    print("product of a digit of a number is:", product)
    print("number in reverse order is:", reversed_number)
    print("sorted number in ascending order is:", sorted_number)
else:
    print("This number isn`t a four-digit natural number")
