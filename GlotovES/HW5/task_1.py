list_int = []
list_float = []
list_length = int(input('input length of your list :'))

for i in range(list_length):
    user_int = int(input(f'input {i+1} integer number: '))
    list_int.append(user_int)

print('This is your integer list:', list_int)

list_float = [float(i) for i in list_int]

print('This is your float list:', list_float)
