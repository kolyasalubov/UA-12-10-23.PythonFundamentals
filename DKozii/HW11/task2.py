def day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[(number - 1) % 7]

try:
    user_input = int(input("Enter the number: "))
    result = day_of_week(user_input)
    print(f"The day of week is: {result}")
except ValueError:
    print("Error! Input a valid number.")
