def rectangle_s(arg1, arg2):
    s = arg1 * arg2
    return f"Square of rectangle is {s} cm^2\n"

def triabgle_s(arg1, arg2):
    s = 0.5 * arg1 * arg2
    print(f"Square of triangle is {s} cm^2\n")

def circle_s(arg):
    PI = 3.14 * arg**2
    s = PI 
    return f"Square of triangle is {s} cm^2\n"


print("Square of rectangle")
side_a = int(input("A: "))
side_b = int(input("B: "))
print(rectangle_s(side_a, side_b))

print("Square of triangle")
side_a = int(input("A: "))
height_h = int(input("H: "))
triabgle_s(side_a, height_h)

print("Square of circle")
radius = int(input("r: "))
square_s = circle_s(radius)
print(square_s)