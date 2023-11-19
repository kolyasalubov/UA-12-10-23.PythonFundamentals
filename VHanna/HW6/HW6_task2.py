login = 'First'

while True:
    user_login = input('Please input your login: ')
    if user_login == login:
        print(f'Hi {login}!')
        break
    else:
        print('Wrong login. Please try again')
        continue
    