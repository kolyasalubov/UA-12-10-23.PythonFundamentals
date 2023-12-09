def processing__age():

    """Is the user_age odd or even"""

    while True:
        try:
            user_age = int(input("Enter your age: "))

            if user_age < 0:
                raise ValueError("Age can not be a negative!")

            if user_age % 2 == 0:
                return "Your age is an even number"
            else:
                return "Your age is an odd number"
        except ValueError as ve:
            print(f"Error: {ve}. Try again.")


print(processing__age())
