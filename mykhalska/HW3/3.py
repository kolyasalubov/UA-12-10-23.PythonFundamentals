value_1 = 'Variable 1'
value_2 = 'Variable 2'

print("Before interchange:")
print("Variable 1: ", value_1, " and Variable 2: ", value_2)

value_1, value_2 = value_2, value_1

print("After interchange: ")
print("Variable 1: ", value_1, " and Variable 2: ", value_2)