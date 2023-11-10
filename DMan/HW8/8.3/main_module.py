from math import pow
from math import pi

def area_of_retraingle():

    """this function calculates area of retraingle by its sides"""
   
    lenght = float(input("Enter the lenght of retraigle:  "))
    width = float(input("Enter the wedth of retraigle:  "))
    # area = lenght * width
    return lenght * width


def area_of_traingle():

    """this function calculates area of traingle by its height and base"""

    height = float(input("Enter the height of traigle:  "))
    base = float(input("Enter the base of retraigle:  "))
    # area = height * base / 2
    return height * base / 2


def area_of_circle():

    """this function calculates area of circle by its radius"""

    radius = float(input("Enter the radius:  "))
    # area = pi * pow(radius, 2)
    return pi * pow(radius, 2)