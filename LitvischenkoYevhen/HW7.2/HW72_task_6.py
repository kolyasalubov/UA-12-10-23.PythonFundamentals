#Reverse List Order
def reverce_list(l: list):
    #return l[::-1]
    l.reverse()
    return l

input_list = list(map(int, (input("Enter list of numbers: ").split())))
print("Input list: ",input_list)
print("Reverce list: ",reverce_list(input_list))