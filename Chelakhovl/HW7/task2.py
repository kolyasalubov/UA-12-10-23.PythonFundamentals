#def calculates_of_rectangle(lenght, width):
#  return lenght * width
#lenght = int(input("Enter the length of the rectangle: "))
#width = int(input("Enter the widht of the rectangle: "))

#result = calculates_of_rectangle(lenght, width)
#print(f"The area of the rectangle is: {result}")


#def calculates_of_triangle(base, height):
#  return base * height / 2
#base = int(input("Enter the base of the triangle : "))
#height = int(input("Enter the height of the triangle: "))

#result = calculates_of_triangle(base, height)
#print(f"The area of the triangle is: {result}")


#NUMBER_PI = 3.14

#def calculates_of_circle (radius):
#  return  NUMBER_PI * radius ** 2
#radius = int(input("Enter the radius of the circle: "))
#result = calculates_of_circle(radius)
#print(f"The area of the circle is: {result}")


def calculates_of_rectangle(lenght, width):
  return lenght * width

def calculates_of_triangle(base, height):
  return base * height / 2

NUMBER_PI = 3.14

def calculates_of_circle (radius):
  return  NUMBER_PI * radius ** 2

print("Select a number figure to calculate the area\n1.Rectangle 2.Triangle 3.Circle")
user_choice = input("Number figure to calculate the area: ")
if user_choice == "1":
  lenght = int(input("Enter the length of the rectangle: "))
  width = int(input("Enter the widht of the rectangle: "))
  result = calculates_of_rectangle(lenght, width)
  print(f"The area of the rectangle is: {result}")
elif user_choice == "2":
  base = int(input("Enter the base of the triangle : "))
  height = int(input("Enter the height of the triangle: "))
  result = calculates_of_triangle(base, height)
  print(f"The area of the triangle is: {result}")
elif user_choice == "3":
  radius = int(input("Enter the radius of the circle: "))
  result = calculates_of_circle(radius)
  print(f"The area of the circle is: {result}")
else:
  print("Erorr: choose the number that corresponds to the figure 1, 2 or 3")

  