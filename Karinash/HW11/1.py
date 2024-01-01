def process_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age % 2 == 0:
            print(f"The entered age {age} is even.")
        else:
            print(f"The entered age {age} is odd.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
user_age = input("Enter your age: ")
process_age(user_age)
