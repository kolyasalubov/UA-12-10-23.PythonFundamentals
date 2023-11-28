def week(day_number):
    if day_number > 7 or day_number < 1:
        raise ValueError("Incorrect number")
    if day_number == 1:
        print("It is Monday")
    elif day_number == 2:
        print("It is Tuesday")
    elif day_number == 3:
        print("It is Wednesday")
    elif day_number == 4:
        print("It is Thursday")
    elif day_number == 5:
        print("It is Friday")
    elif day_number == 6:
        print("It is Saturday")
    else:
        print("It is Sunday")


day = int(input("Write day of week as number form 1 to 7:\n"))
try:
    week(day)
except ValueError as e:
    print(e)
