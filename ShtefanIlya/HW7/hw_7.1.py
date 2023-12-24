#Var_1
def maxNum(arg1:int(), arg2:int()) -> str():
    """
    The function returns
    the largest number 
    of two numbers
    """
    if arg1 > arg2:
        return f"The A:{arg1} is largest number"
    elif arg1 == arg2:
        return "Both numbers are equal"
    else:
        return f"The B:{arg2} is largest number"
    
num_a = int(input("A: "))
num_b = int(input("B: "))

print(maxNum(num_a, num_b))


#Var_2
# def maxNum(arg1:int(), arg2:int()) -> str():
#     """
#     The function returns
#     the largest number 
#     of two numbers
#     """
#     if arg1 > arg2:
#         print(f"The A:{arg1} is largest number") 
#     elif arg1 == arg2:
#         print("Both numbers are equal")
#     else:
#         print(f"The B:{arg2} is largest number")
    
# num_a = int(input("A: "))
# num_b = int(input("B: "))

# maxNum(num_a, num_b)


#Var_3
# def maxNum(l: list()) -> int():
#     """
#     This function search
#     the max element in a list
#     """
#     return f"The max number is {max(l)}"


# nums = []
# for i in range(2):
#     num = int(input(f"Enter num #{i+1}: "))
#     nums.append(num)

# print(maxNum(nums))

