import areas

print("Hi! Choose your figure: \n1.Rectangle \n2.Triangle \n3.Circle")
m = int(input("Choose the number:"))
if m > 3:
    print(f"Sorry, there's no option {m}, try one more time!")
elif m == 1 :
    a = float(input("Enter width of the rectangle: "))
    b = float(input("Enter length of the rectangle: "))
    c = areas.count_rect_area(a,b)
    print(f"Area of this rectengle is {c}")
elif m == 2 :
    a = float(input("Enter hight of the triangle: "))
    h = float(input("Enter length of the triangle: "))
    c = areas.count_triangle_area(a,h)
    print(f"Area of this triangle is {c}")
elif m == 3 :
    r = float(input("Enter radius of the circle: "))
    c = areas.count_circle_area(r)
    print(f"Area of this circle is {c}")