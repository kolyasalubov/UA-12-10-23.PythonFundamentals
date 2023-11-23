def check_day_of_week(num):
    if not isinstance(num, int):
        raise ValueError("Enter a valid numerical value.")
    
    if 1 <= num <= 7:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[num - 1]
    else:
        return "Error. Please enter a number between 1 and 7."

def main():
    try:
        num = int(input("Enter a number (1-7) to get the check day of the week: "))
        day = check_day_of_week(num)
        print(f"The day of the week is: {day}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
