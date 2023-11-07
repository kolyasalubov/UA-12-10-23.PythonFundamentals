#Are You Playing Banjo?
def banjo_playing(name: str):
    """banjo plays only whos naim start with 'R' or 'r'"""
    if name[0] == 'R' or name[0] == 'r' :
        print(f'{name} plays banjo')
    else:
        print(f'{name} does not plays banjo')
    

input_name = input("Enter your name :")
banjo_playing(input_name)