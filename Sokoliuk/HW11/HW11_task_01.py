# class CustomError(Exception):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)

def age_info(age):
    if age % 2 == 0:
        print("Your age is even\n")
    else:
        print("Your age is odd\n")


print("Hi user, we need to know your age\n")

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            # raise CustomError("Your age can't be less than 0")
            raise Exception("Your age can't be less than 0")
    except ValueError:
        print("Only digits allowed")
    else:
        age_info(age)
        break
