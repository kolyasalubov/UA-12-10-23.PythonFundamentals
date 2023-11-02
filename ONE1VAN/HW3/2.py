while True:
    number = input('Enter four-digit number: \t')
    product = 1
    if len(number) == 4 and number.isdigit():
        for i in number:
            product *= int(i)
        print(f'Product of your number is: {product}')
        print(f'Your reversed number is: {number[::-1]}')
        print(f'Your sorted number is: {sorted(number)}')
        break
    else:
        print("Your input is incorrect!")





