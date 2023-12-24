from math import pi

#area of rectangle =  a * b (sides)
#area of triangle = 0.5 * a * h
#area of  circle = s 3.14 * r**2

# V_1

# def areaRectangle(side_a, side_b):
#     res = side_a * side_b
#     print("Result =", res)

# def areaTriangle(side_a, heigt_h):
#     res = 0.5 * side_a * heigt_h
#     print("Result =", res)

# def areaCircle(rad_r):
#     res = pi * rad_r
#     print("Result =", res)


# print("""
#     Rectangle;
#     Triangle;
#     Circle;
# """)

# area = input("Enter an area you want to find: ")
# area = area.lower()

# match area:
#     case "rectangle":
#         a = int(input("Enter side a: "))
#         b = int(input("Enter side b: "))
#         areaRectangle(a, b)
    
#     case "triangle":
#         a = int(input("Enter side a: "))
#         h = int(input("Enter height h: "))
#         areaTriangle(a, h)
    
#     case "circle":
#         r = int(input("Enter radius r: "))
#         areaCircle(r)
    
#     case _:
#         print("Invalid value!")



# V_2

# from math import pi
# def areaRectangle():
#     a = int(input("Enter side a: "))
#     b = int(input("Enter side b: "))
#     res = a * b
#     print("Result =", res)

# def areaTriangle():
#     a = int(input("Enter side a: "))
#     h = int(input("Enter height h: "))
#     res = 0.5 * a * h
#     print("Result =", res)

# def areaCircle():
#     r = int(input("Enter radius r: "))
#     res = pi * r
#     print("Result =", res)



# print("""
#     Rectangle;
#     Triangle;
#     Circle;
# """)

# area = input("Enter an area you want to find: ")
# area = area.lower()

# if area == "rectangle":
#     areaRectangle()
# elif area == "triangle":
#     areaTriangle()
# elif area == "circle":
#     areaCircle()





# V_3

def main(s):
    
    def areaRectangle():
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        res = a * b
        print("Result =", res)

    def areaTriangle():
        a = int(input("Enter side a: "))
        h = int(input("Enter height h: "))
        res = 0.5 * a * h
        print("Result =", res)

    def areaCircle():
        r = int(input("Enter radius r: "))
        res = pi * r**2
        print("Result =", res)
    
    if s == "rectangle":
        areaRectangle()
    elif s == "triangle":
        areaTriangle()
    elif s == "circle":
        areaCircle()

print("""
    Rectangle;
    Triangle;
    Circle;
""")

area = input("Enter an area you want to find: ")
area = area.lower()

main(area)