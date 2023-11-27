def checking(number):
    try:
        number = int(number)
        if number <=0 or number >=120:
            print('You typed wrond age ') # or raise ValueError('You typed wrond number ')
            return False
        else:
            return True
    except ValueError:
        print('You entered not a age')
        return False

def is_odd(age):
    if age %2 == 1:
        return True
    return False
while True:
    input_ = input("Enter your age: ")
    if checking(input_):
        print(f'Your age is odd: {is_odd(int(input_))}')
        break


