class CustomError(Exception):
    
    def __str__(self):
        return repr(self)


def get_day_week(input_data):
    day_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"}
    return f"{input_data} is {day_week[input_data]}"


while True:
    try:
        input_data = int(input("Enter the number of the day week: "))
        if input_data < 1 or input_data > 7:
            raise CustomError
    except ValueError:
        print("Enter only digits!\n")
    except CustomError:
        print("Use only numbers from 1 to 7")
    else:
        print(get_day_week(input_data))
        break
