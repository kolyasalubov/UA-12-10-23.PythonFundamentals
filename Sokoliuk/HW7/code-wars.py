# Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    
# Find The Distance Between Two Points

import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2+(y2-y1)**2),2)

# No yelling!

def filter_words(st):
    st = st.lower()
    st = st.capitalize()
    st = ' '.join(st.split())
    return st

# Convert a Number to a String!

def number_to_string(num):
    return str(num)

# Reversing Words in a String

def reverse(st):
    st = st.split()
    st.reverse()
    st = ' '.join(st)
    
    return st

# Reverse List Order

def reverse_list(l):
    return l[::-1]

# Multiples of 3 or 5

def solution(number):
    if number < 0:
        return 0
    sum = 0
    for element in range(number):
        if element % 3 == 0 or element % 5 == 0:
            sum += element
        else:
            continue
    
    return sum

# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg*fuel_left:
        return True
    else:
        return False
    
# Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name.lower().startswith("r"):
        return name + " plays banjo"
    return name + " does not play banjo"

# Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    return "Yes" if boolean is True else "No"

# Counting sheep...

def count_sheeps(sheep):
    counter = 0
    for element in sheep:
        if element == True:
            counter += 1
    return counter

# Is this my tail?

def correct_tail(body, tail):
    return True if body.endswith(tail) else False
