def rec_area(a_side, b_side):
    return a_side * b_side

def tri_area(a_side, b_side, c_side):
    half_per = (a_side + b_side + c_side)/2
    return round((half_per * (half_per - a_side) * (half_per - b_side) * (half_per - c_side))**(1/2),2)

def cir_area(radius):
    PI = 3.14
    return PI * radius**2


which = input("Enter a figure you want to calculate the area: \t")
which = which.lower()

if which == 'rectangle':
    side_a = int(input("Enter side a: \t"))
    side_b = int(input("Enter side b: \t"))
    print(rec_area(side_a, side_b))
elif which == 'triangle':
    side_a = int(input("Enter side a: \t"))
    side_b = int(input("Enter side b: \t"))
    side_c = int(input("Enter side c: \t"))
    print(tri_area(side_a, side_b, side_c))
elif which == 'circle':
    radius = int(input("Enter radius: \t"))
    print(cir_area(radius))
