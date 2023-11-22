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

    try:
        number = int(number)

        if 1 <= number <= 7:
            day = days_of_week[number]
            print(f"The day of the week for {number} is {day}.")
        else:
            print("Error: Please enter a number between 1 and 7.")
    except ValueError:
        print("Error: Please enter a numerical value.")


user_input = input("Enter a number to get the day of the week: ")
get_day_of_week(user_input)
