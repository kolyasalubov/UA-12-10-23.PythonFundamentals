import areas

print("Hello, of what figure area you want to calculate? ")
print("""
This program can work with:
\trectangle area
\ttriangle area
\tcircle area
""")
figure = input("Choose the figure: ")

if figure == "rectangle":
    length = float(input("Length: "))
    width = float(input("Width: "))
    print(f"{areas.rectangle(length, width):.3f}")

elif figure == "triangle":
    height = float(input("Height: "))
    base = float(input("Base: "))
    print(f"{areas.triangle(height, base):.3f}")

elif figure == "circle":
    radius = float(input("Radius: "))
    print(f"{areas.circle(radius):.3f}")

else:
    print("Unknown figure")