#Reverse List Order
def reverce_list(l: list):
    """Reverse list"""
    #return l[::-1]
    l.reverse()
    return l

#Enter strin of numbers and convert to list of int
input_list = list(map(int, (input("Enter list of numbers: ").split())))
print("Input list: ",input_list)
print("Reverce list: ",reverce_list(input_list))