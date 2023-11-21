#ver 1
def largest_num(lst):
    """
    function accept a list()
    and return int() 
    """
    return f"largest number is {max(lst)}" 


l = []
for el in range(2):
    number = int(input(f"Enter a number {el+1}: "))
    l.append(number)
print(largest_num(l))


# ver_2
# def largest_num(lst: list()) -> int():
#     print(f"largest number is {max(lst)}")
    
    
# l = []
# for el in range(2):
#     number = int(input(f"Enter a number {el+1}: "))
#     l.append(number)
# largest_num(l)


# ver_3
# def largest_num(arg1: int(), arg2: int()) -> int():
#     if arg1 > arg2:
#         return f"{arg1} is largest number"
#     elif arg1 < arg2:
#         return f"{arg2} is largest number"
#     else:
#         return "Both numbers are equal"


# num1 = input("Enter a number1: ")
# num2 = input("Enter a number2: ")
# print(largest_num(num1, num2))