import logging

logging.basicConfig(level=logging.INFO)

def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be a negative number.")
    elif age % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        result = process_age(age)
        logging.info(f"The age {age} is {result}.")
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()