import math


def area_of_rectangle():
    length = int(input("Enter length of rectangle:\n"))
    width = int(input("Enter width of rectangle:\n"))
    res = length*width
    print(f"Area of rectangle = {res}")
    pass


def area_of_triangle():
    base = int(input("Enter base of rectangle:\n"))
    height = int(input("Enter height of rectangle:\n"))
    res = (base * height) / 2
    print(f"Area of triangle = {res}")
    pass


def area_of_circle():
    radius = int(input("Enter radius of rectangle:\n"))
    res = math.pi * math.pow(radius, 2)
    print(f"Area of circle = {res}")
    pass


inp = input("What area of you want to find?\nrectangle, triangle or circle?\n")
if inp == "rectangle":
    area_of_rectangle()
elif inp == "triangle":
    area_of_triangle()
elif inp == "circle":
    area_of_circle()
