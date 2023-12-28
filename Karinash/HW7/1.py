def find_largest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

number1 = 15
number2 = 23
result = find_largest_number(number1, number2)
print(f"The largest number between {number1} and {number2} is: {result}")
