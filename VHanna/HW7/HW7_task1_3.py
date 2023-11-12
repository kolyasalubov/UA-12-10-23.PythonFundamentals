def number_of_characters(input_string):
    num_count = {}
    
    for i in input_string:
        num_count[i.lower()] = num_count.get(i.lower(), 0) + 1

    return num_count

input_string = input('Enter world: ')
result = number_of_characters(input_string)
print(result)
