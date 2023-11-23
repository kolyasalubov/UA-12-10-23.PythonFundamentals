def check_odd_even_age(age):
    age = int(age)
    print(age)
    if age < 0 :
        raise ValueError('Age is negative')
    if age % 2 == 0:
        print("Your age is even")
    else:
        print("Your is odd")
          
while True:
    num = input("Enter the age: ")
    if num == 'q': break
    try:    
        check_odd_even_age(num)
    except ValueError as e:
        print(e)