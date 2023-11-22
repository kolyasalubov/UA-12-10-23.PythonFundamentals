def code_verification(age):
    if age < 0:
        return "Age cannot be a negative number"
    elif age % 2 == 0:
        return "even"
    else:
        return "odd"

def input_user():
    try:
        age = int(input("Enter your age: "))
        result = code_verification(age)
        print(f"Your age is {result}")
    except ValueError:
        print("Please enter a valid integer for your age.")


input_user()
