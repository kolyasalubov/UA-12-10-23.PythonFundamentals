#Jenny's secret message
def greeting(name):
    """greeting user with exept"""
    if name.lower() == 'johnny' :
        print(f'I lOVE YOU JOHNNY!!!')
    else:
        print(f'Hello, {name.capitalize()}!')

input_name = input("Enter your name :")
greeting(input_name)
