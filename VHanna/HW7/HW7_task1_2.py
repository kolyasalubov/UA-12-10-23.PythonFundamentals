def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14159 * radius**2

shape = int(input('Choose a shape: 1. Rectangle / 2. Triangle / 3. Circle :  '))

if shape == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    result = rectangle_area(length, width)
elif shape == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    result = triangle_area(base, height)
elif shape == 3:
    radius = float(input("Enter the radius of the circle: "))
    result = circle_area(radius)
else:
    print("Error. Please enter 1, 2, or 3.")
    result = None

if result is not None:
    print(f"The area of {shape} is: {result}")
