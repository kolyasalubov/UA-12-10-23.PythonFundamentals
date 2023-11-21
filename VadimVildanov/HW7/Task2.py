import math


def area_rectangle(length, width):
    """
    This function calculates the area of a rectangle. To calculate the area of a rectangle, we need to
    multiply the length by the width.
    """
    return length * width


def area_triangle(base, height):
    """
    This function calculates the area of a triangle. To calculate the area of a triangle, we need to
    multiply the base by the height, and divide by two.
    """
    return (base * height) / 2


def area_circle(radius):
    """
    In order to find the area of a circle, it is necessary to multiply the number Pi by the square of its radius.
    """
    return math.pi * math.pow(radius,2)


change = input("Enter area you need? \n rectangle, triangle, circle ? \n")

if change == "rectangle":
    length = int(input("Enter length rectangle: "))
    width = int(input("Enter width rectangle: "))
    print("Area your rectangle is: ", area_rectangle(length, width))

elif change == "triangle":
    base = int(input("Enter base triangle: "))
    height = int(input("Enter height triangle: "))
    print("Area your triangle is: ", area_triangle(base, height))
elif change == "circle":
    radius = int(input("Enter radius circle: "))
    print("Area your circle is: ", area_circle(radius))