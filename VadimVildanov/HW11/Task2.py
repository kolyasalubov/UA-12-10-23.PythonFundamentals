def get_day_of_week(number):
    if not isinstance(number, int):
        raise ValueError("Input must be a numerical value")

    if number < 1:
        raise ValueError("Number must be 1 or greater")

    if number <= 7:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"The corresponding day of the week for {number} is {days_of_week[number - 1]}.")
    else:
        remainder = (number - 1) % 7
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"The corresponding day of the week for {number} is {days_of_week[remainder]}.")


"""
The get_day_of_week function takes an input number, checks if it's an integer and within the valid range. 
It then calculates and prints the corresponding day of the week
"""


def main():
    try:
        user_input = input("Enter a number to get the day of the week: ")
        user_number = int(user_input)
        get_day_of_week(user_number)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


"""
The main function is the entry point of the program. It uses a try-except block to handle potential exceptions, 
such as a ValueError if the user enters non-numerical data
"""

if __name__ == "__main__":
    main()
"""
The __name__ == "__main__": condition ensures that the main function is only called if the script is run 
directly and not imported as a module
"""