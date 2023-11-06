#Convert boolean values to strings 'Yes' or 'No'.
def bool_convert(value: bool):
    """Convert bool to string"""
    if value :
        return "Yes"
    else:
        return "No"
    
value = int(input("Take your choce True(1) or False(0): "))
print(f"Your chois is : {bool_convert(value)}")
    
