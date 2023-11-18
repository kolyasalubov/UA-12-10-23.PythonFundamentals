def find_the_largest(num1, num2):
    """
    Returns the largest number of two given numbers.
    In case both numbers are equal, it informs the user.
    """
    if num1 > num2:
        return print(f"{num1} is bigger than {num2} ")
    elif num1 < num2:
        return print(f"{num2} is bigger than {num1} ")
    else:
        return print(f"{num1} equals to {num2} ")

print(find_the_largest.__doc__)

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

find_the_largest(num1, num2)
