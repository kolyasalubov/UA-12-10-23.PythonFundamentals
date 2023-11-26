def area_rectangle(lenght, width):
    area = lenght * width
    print(area)
    return area
lenght = 10
width = 15
area_rectangle(lenght, width)

def area_triangle(side1, side2):
    area = 0.5 * side1 * side2
    print(f"{area:.2f}")
    return area
side1 = 17.1
side2 = 12
area_triangle(side1, side2)


def area_circle(PI, radius):
    area = PI * (radius ** 2)
    print(f"{area:.2f}")
    return area
PI = 3.14159265358979
radius = 15
area_circle(PI, radius)

