def largest_num(first, second):
    '''
    Comparison of two numbers
    param first --> int
    param second --> int
    return --> int or str
    '''
    if first > second:
        return first
    elif first == second:
        return 'first = second'
    else:
        return second

first_num, second_num = input('Input first number '), input('Input second number ')
print(largest_num(first_num, second_num))
