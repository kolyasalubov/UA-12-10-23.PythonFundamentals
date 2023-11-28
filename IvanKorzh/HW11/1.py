def even_odd(age_fun):
    if age_fun < 0:
        raise ValueError('Age is negative')
    if age_fun % 2 == 0:
        return "even"
    else:
        return "odd"


age = int(input("Enter your age:"))
try:
    age = even_odd(age)
    print(f"Your age is {age} number")
except ValueError as e:
    print(e)
