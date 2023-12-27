import logging

logging.basicConfig(level=logging.INFO)

def get_day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if not isinstance(number, int):
        raise ValueError("Please enter a numerical value.")
    elif number < 1 or number > 7:
        raise ValueError("Please enter a number between 1 and 7.")
    
    return days[number - 1]

def main():
    try:
        user_input = input("Enter a number (1-7) to get the corresponding day of the week: ")
        day_number = int(user_input)
        day_name = get_day_of_week(day_number)
        logging.info(f"The day corresponding to the number {day_number} is {day_name}.")
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()