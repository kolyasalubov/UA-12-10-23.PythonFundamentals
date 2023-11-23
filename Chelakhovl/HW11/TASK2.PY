def get_day_of_week(number):
    days_of_week = ["0", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if 1 <= number <= 7:
        return days_of_week[number]
    else:
        return "Invalid number. Please enter a number from 1 to 7."


def input_and_analyze():
    try:
        number = int(input("Enter a number (1-7): "))
        result = get_day_of_week(number)
        print(f"{number} is {result}")
    except ValueError:
        print("Invalid number. Please enter an integer from 1 to 7.")


input_and_analyze()
