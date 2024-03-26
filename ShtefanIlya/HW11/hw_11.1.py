def verification(number):
    if number < 0:
        raise ValueError("Number must be bigger or equal 0!")
    elif number == 0:
        print("You enter 0!")
    else:
        print("Your age is {}".format(number))
        
                
try:      
    user_age = int(input("Enter your age: "))
    verification(user_age)        
except ValueError as e:
    print(e)




# variant 2
# def verification(number):
#     if number < 0:
#         print("Number must be bigger or equal 0!")
#     elif number == 0:
#         print("You enter 0!")
#     else:
#         print("Your age is {}".format(number))
        
                
# try:      
#     user_age = int(input("Enter your age: "))
#     verification(user_age)
        
# except ValueError:
#     print("You should to enter a bumber, NOT letter!")
