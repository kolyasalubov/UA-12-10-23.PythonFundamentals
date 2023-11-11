from main_module import *

while True:

    print("Hello! The area of which shape do you want to calculate?")
    print("1. Rectangle\n2. Tringle\n3. Circle")
    # print("'q' to Exit")
    choice = input('Enter the number of shape or "q" to Exit:  ')  
    
    match choice:
        case "1":
            print(area_of_retraingle())
        case "2":
            print(area_of_traingle())
        case "3":
            print(area_of_circle())
        case "q":
            break
        case _:
            print("invalid input")