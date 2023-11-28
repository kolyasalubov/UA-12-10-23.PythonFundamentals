# Task 1
def get_largest_number(num1, num2):
    """
    Returns the largest number of two numbers.
    Parameters:
    - num1 (float or int): The first number.
    - num2 (float or int): The second number.
    Returns:
    - float or int: The largest number.
    """
    return max(num1, num2)


# Task 2
def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.
    Parameters:
    - length (float or int): The length of the rectangle.
    - width (float or int): The width of the rectangle.
    Returns:
    - float or int: The area of the rectangle.
    """
    return length * width


def calculate_triangle_area(base, height):
    """
    Calculates the area of a triangle.
    Parameters:
    - base (float or int): The base of the triangle.
    - height (float or int): The height of the triangle.
    Returns:
    - float or int: The area of the triangle.
    """
    return 0.5 * base * height


def calculate_circle_area(radius):
    """
    Calculates the area of a circle.

    Parameters:
    - radius (float or int): The radius of the circle.

    Returns:
    - float or int: The area of the circle.
    """
    import math
    return math.pi * radius**2


# Task 3
def count_characters(input_string):
    """
    Calculates the number of characters included in the given string.

    Parameters:
    - input_string (str): The input string.

    Returns:
    - dict: A dictionary containing each unique character as a key and its count as a value.
    """
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


######################################################################
print(get_largest_number(5, 10))

######################################################################
choice = input("Enter shape (rectangle, triangle, or circle): ").lower()
if choice == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of rectangle:", calculate_rectangle_area(length, width))
elif choice == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle:", calculate_triangle_area(base, height))
elif choice == "circle":
    radius = float(input("Enter radius: "))
    print("Area of circle:", calculate_circle_area(radius))
else:
    print("Invalid choice")

#####################################################################
input_str = "hello"
print(count_characters(input_str))
