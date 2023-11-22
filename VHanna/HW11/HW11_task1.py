def check_age(age):
    if age < 0:
        raise ValueError("Age must be a non-negative number.")
    
    if age % 2 == 0:
        print(f"The age {age} is even.")
    else:
        print(f"The age {age} is odd.")

def main():
    try:
        age = int(input("Enter your age: "))
        check_age(age)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
