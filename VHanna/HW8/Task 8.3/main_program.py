import math_module

def get_figure_area():
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    shape = input("Enter the number of the figure: ")

    if shape == "1":
        a = float(input("Enter the length of side 'a': "))
        b = float(input("Enter the length of side 'b': "))
        result = math_module.rectangle_area(a, b)
        print(f"The area of the rectangle is: {result}")

    elif shape == "2":
        base = float(input("Enter the length of the base: "))
        height = float(input("Enter the height: "))
        result = math_module.triangle_area(base, height)
        print(f"The area of the triangle is: {result}")

    elif shape == "3":
        radius = float(input("Enter the radius: "))
        result = math_module.circle_area(radius)
        print(f"The area of the circle is: {result}")

    else:
        print("Error. Please enter a valid number.")

if __name__ == "__main__":
    get_figure_area()