import math

def rectangle(length, width):
    return length * width

def triangle(height, base):
    return 0.5 * height * base

def circle(radius):
    return math.pi * math.pow(radius, 2)

print(circle(25))