#Jenny's secret message
def greeting(name):
    if name.lower() == 'johnny' :
        print(f'I lOVE YOU JOHNNY!!!')
    else:
        print(f'Hello, {name.capitalize()}!')

verifi_name = input("Enter your name :")
greeting(verifi_name)
