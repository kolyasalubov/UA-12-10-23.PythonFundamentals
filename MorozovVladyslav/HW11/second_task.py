def checking(number):
    try:
        number = int(number)
        if number <1 or number >=7:
            print('You typed wrond number ') # or raise ValueError('You typed wrond number ')
            return False
        else:
            return True
    except ValueError:
        print('You entered not a number')
        return False
    
days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'

]

dict_ = dict(enumerate(days,1))

while True :
    input_ = input('Enter number : ')
    day = checking(input_)
    if day:
        answer = dict_[int(input_)]
        break

print(answer)
