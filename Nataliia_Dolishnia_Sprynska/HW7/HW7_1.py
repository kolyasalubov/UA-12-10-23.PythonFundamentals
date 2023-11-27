def find_largest_number(num1, num2):
    """
    Find the largest number between two given numbers.

    Parameters:
    - num1 (int or float): The first number.
    - num2 (int or float): The second number.

    Returns:
    int or float: The largest number between num1 and num2.
    """
    return max(num1, num2)

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = find_largest_number(number1, number2)
print(f"The largest number is: {result}")