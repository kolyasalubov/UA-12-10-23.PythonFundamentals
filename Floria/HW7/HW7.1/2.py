import math


def area_of_rectangle():
    lenght = float(input("Enter the length of the rectangle:\n"))
    width = float(input("Enter the widht of the rectangle:\n "))
    result = lenght * width
    print(f"The area of the rectangle is: {result}")


def area_of_triangle():
    height = float(input("Enter the height of the triangle:\n"))
    base = float(input("Enter the base of the triangle:\n"))
    result = 1/2 * height * base
    print(f"The area of the triangle is: {result}")


def area_of_circle():
    radius = float(input("Enter the radius of the circle:\n"))
    result = math.pi * radius ** 2
    print(f"The area of the triangle is: {result}")


i = input("What shape do you want to know the area of? A rectangle? A triangle? A circle?\n")
if i == "rectangle":
    area_of_rectangle()
elif i == "triangle":
    area_of_triangle()
elif i == "circle":
    area_of_circle()
else:
    print("Error: There are only three options")
