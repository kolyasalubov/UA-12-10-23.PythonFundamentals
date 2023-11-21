a = int(input("Input fisrt number: "))
b = int(input("Input second number: "))

def largest_number(f_num, s_num):
    
    '''
    Function returns the largest number of two numbers
    '''
    
    if f_num > s_num:
        return print(f"{f_num} is biggest then {s_num}")
    elif s_num > f_num:
        return print(f"{s_num} is biggest then {f_num}")
    else: 
        return print("both number are the same")
        
largest_number(a, b)
