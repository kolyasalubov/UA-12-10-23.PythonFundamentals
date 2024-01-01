def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age % 2 == 0:
        print(f"The entered age {age} is even.")
    else:
        print(f"The entered age {age} is odd.")


"""
The process_age function takes an age as an argument, checks if it's negative, 
and then prints whether it's even or odd
"""


def main():
    try:
        user_age = int(input("Enter your age: "))
        process_age(user_age)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


"""
The main function is the entry point of the program. It uses a try-except block to handle potential exceptions, 
such as a ValueError if the user enters a non-integer or a negative number
"""


if __name__ == "__main__":
    main()

"""
The __name__ == "__main__": condition ensures that the main function is only called if the script is run 
directly and not imported as a module
"""