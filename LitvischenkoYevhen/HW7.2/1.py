def greet(name):
    """
    Jenny has written a function that returns a greeting for a user.
    However, she's in love with Johnny, and would like to greet him slightly different.
    She added a special case to her function, but she made a mistake.
    """
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

def distance(x1, y1, x2, y2):
    """
    Given two ordered pairs calculate the distance between them. Round to two decimal places.
    This should be easy to do in 0(1) timing.
    """
    return round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)

def distans(a: list, b: list) -> float:
    """
    Distance Between Two Points
    a -> list[0, 1]
    b -> list[0, 1]
    return -> float:2
    """
    return round(((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5, 2)


#def filter_words(str):
#    """Capitalized string and remove unneedible space"""
#    return ' '.join(str.split()).capitalize()

def filter_words(str):
    """
    Write a function taking in a string like 'WOW this is REALLY          amazing '
    and returning 'Wow this is really amazing'.
    String should be capitalized and properly spaced. Using re and string is not allowed.
    """
    alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #alphabet_lower = list(''.join(alphabet_upper).lower())
    alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #convert string to list
    list_of_char = list(str)
    #Delite spaces
    while list_of_char[0] == ' ' :
        list_of_char.pop(0)
    while list_of_char[-1] == ' ' :
        list_of_char.pop(-1)
    i = 0    
    while i < len(list_of_char) :
        if list_of_char[i] == ' ' and list_of_char[i-1] == ' ':
            list_of_char.pop(i)
        else:
            i += 1    
    #Capitalized list
    for i in range(len(list_of_char)) :
        if i == 0:
            if list_of_char[i] in alphabet_lower:
                list_of_char[i] = alphabet_upper[alphabet_lower.index(list_of_char[i])]
        elif list_of_char[i] in alphabet_upper:
            list_of_char[i] = alphabet_lower[alphabet_upper.index(list_of_char[i])]
    #concatinate string from list
    result_str = ''
    for i in list_of_char :
        result_str += i
    return result_str

def number_to_string(num):
    """
    We need a function that can transform a number (integer) into a string.
    What ways of achieving this do you know?
    """
    st_1 = str(num)
#    st_2 = f'{num}'
#    st_3 = '{}'.format(num)
    return st_1

def reverse(st):
    """
    You need to write a function that reverses the words in a given string.
    A word can also fit an empty string. If this is not clear enough, here are some examples:
    As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
    """
    return ' '.join(reversed(st.split()))

def reverce_list(l: list):
    """In this kata you will create a function that takes in a list and returns a list with the reverse order."""
    return l[::-1]

def solution(number):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
    Additionally, if the number is negative, return 0.
    Note: If the number is a multiple of both 3 and 5, only count it once.
    """
    if number < 0 :
        return 0
    return sum([x for x in range(1, number) if (x%3 == 0) or (x%5 == 0)])
  
def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
    Considering these factors, write a function that tells you if it is possible to get to the pump or not.
    Function should return true if it is possible and false if not.
    """
    if fuel_left*mpg >= distance_to_pump:
        return True
    else:
        return False
    
def are_you_playing_banjo(name):
    """
    Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!
    The function takes a name as its only argument, and returns one of the following strings:
    """
    if name[0] == 'R' or name[0] == 'r' :
        name += ' plays banjo'
    else:
        name += ' does not play banjo'
    return name

def bool_to_word(boolean):
    """Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false."""
    return "Yes" if boolean else "No"

def count_sheeps(sheep):
    """
    Consider an array/list of sheep where some sheep may be missing from their place.
    We need a function that counts the number of sheep present in the array (true means present).
    """
    return sheep.count(True)

