def calculate_characters(string):
    # string = string.lower()               # if you don't need uppercase letters
    dict_of_string = {}
    for element in string:
        if element not in dict_of_string:
            dict_of_string[element] = 1
        else:
            dict_of_string[element] += 1
    
    return dict_of_string

string = input("Hi, enter the string: ")

print(calculate_characters(string))