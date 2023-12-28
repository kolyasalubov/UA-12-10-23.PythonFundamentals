def find_largest_number(num1, num2):
    """
    Finds and returns the largest number between two given numbers.
    Parameters:
    - num1 : The first number.
    - num2 : The second number.
    Returns:
    The largest number between num1 and num2.
    """
    if num1 > num2:
        return num1
    else:
        return num2

number1 = 15
number2 = 22
largest_number = find_largest_number(number1, number2)
print(f"The largest number between {number1} and {number2} is: {largest_number}")