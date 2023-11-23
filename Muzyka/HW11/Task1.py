def process_age(age):
    if age < 0:
        raise ValueError("Error: Age cannot be negative.")
    else:
        message = "Odd age." if age % 2 == 0 else "Even age."
        print(message)


try:
    age = int(input("Input your age: "))

    process_age(age)

except ValueError as e:
    print("Error:", e)
