import math

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius**2

print("Choose a shape to calculate its area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter the number corresponding to your choice: "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is: {area}")
elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area}")
else:
    print("Invalid choice. Please enter a valid number.")
