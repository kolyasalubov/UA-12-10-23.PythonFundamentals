int_list = []
float_list = []
count = 0

many = int(input('Enter how many elements you want in your list: \t'))
print(f'You need to enter {many} elements of list')

while count < many:
    try:
        elements = int(input('Enter element(number) of list: \t'))
        int_list.append(elements)
        count += 1
    except ValueError:
        print('You need to enter numbers! Try again')


for element in int_list:
    element = float(element)
    float_list.append(element)

print(f'Your int list is: {int_list}')
print(f'Your float list is: {float_list}')
