import areas

print("Select a shape:\n1.Rectangle \n2.Triangle \n3.Circle")

shape = input("Number figure to calculate the area: ")
if shape == 1:
  lenght = int(input("Enter the length of the rectangle: "))
  width = int(input("Enter the widht of the rectangle: "))
  result = areas.rectangle_area(lenght, width)
  print(f"The area of this rectengle is {result}")
elif shape == 2:
  base = int(input("Enter the base of the triangle : "))
  height = int(input("Enter the height of the triangle: "))
  result = areas.triangle_area(base, height)
  print(f"The area of this triangle is: {result}")
elif shape == 3:
  radius = int(input("Enter the radius of the circle: "))
  result = areas.circle_area(radius)
  print(f"The area of this circle is: {result}")
else:
  print("Invalid choice. Please enter 1, 2, 3")