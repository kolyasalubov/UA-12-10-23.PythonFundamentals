import math


def area_circle():
    radius = int(input("Enter radius of rectangle:\n"))
    res = math.pi * math.pow(radius, 2)
    print(f"Area of circle = {res}")
