def get_day_of_week(number):
    try:
        day_number = int(number)
        if 1 <= day_number <= 7:
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(f"The corresponding day for {day_number} is {days_of_week[day_number - 1]}.")
        else:
            raise ValueError("Invalid day number. Please enter a number between 1 and 7.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
user_number = input("Enter a number (1-7) to get the corresponding day of the week: ")
get_day_of_week(user_number)
