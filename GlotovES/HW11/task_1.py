def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be a negative number.")
    elif age % 2 == 0:
        print("The entered age is even.")
    else:
        print("The entered age is odd.")

def main():
    try:
        age = int(input("Enter your age: "))
        process_age(age)
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()