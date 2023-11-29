def get_day_of_week(number):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if isinstance(number, int):
        if 1 <= number <= 7:
            return days_of_week[number]
        else:
            return "Invalid input. Please enter a number between 1 and 7."
    else:
        return "Invalid input. Please enter a numerical value."

def main():
    try:
        user_input = input("Enter a number (1-7) to get the corresponding day of the week: ")
        number = int(user_input)
        result = get_day_of_week(number)
        print(f"The day of the week is: {result}")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()