__all__ = ['area_rectangle', 'area_triangle', 'area_circle']

from math import pi, pow

def area_rectangle(side_1, side_2):
    """return area of rectangle"""
    area = side_1 * side_2
    return area

def area_triangle(base, higth):
    """return area of triangle"""
    area = base * higth/2
    return area

def area_circle(radius):
    """return area of circle"""
    area = round(pi* pow(radius, 2), 2)    
    return area