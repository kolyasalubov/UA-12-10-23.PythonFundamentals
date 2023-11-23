def day_of_week(number):
    try:
        number = int(number)
        if 1 <= number <= 7:
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(f"Day of the week: {days_of_week[number-1]}")
        else:
            print("Your numnet out of range")
    except ValueError:
        print("You enter incorrect number")

while True:
    day = input("Enter the number (1-7): ")
    if day == 'q' : break
    day_of_week(day)
