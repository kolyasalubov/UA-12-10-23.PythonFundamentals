value_1 = input('Enter value_1 : ')
value_2 = input('Enter value_2 : ')
print('\n Before interchange :')
print(f'value_1 :{value_1}   ID :{id(value_1)}')
print(f'value_2 :{value_2}   ID :{id(value_2)}')
value_1, value_2 = value_2, value_1
print('\n After interchange :')
print(f'value_1 :{value_1}   ID :{id(value_1)}')
print(f'value_2 :{value_2}   ID :{id(value_2)}')