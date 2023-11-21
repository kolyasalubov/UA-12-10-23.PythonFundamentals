import math


# 1 Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.
# Can you help her?
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


# 2 Given two ordered pairs calculate the distance between them.
# Round to two decimal places.
# This should be easy to do in 0(1) timing.
def distance(x1, y1, x2, y2):
    res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(res, 2)


# 3Write a function taking in a string like "WOW this is REALLY          amazing"
# and returning "Wow this is really amazing".
# String should be capitalized and properly spaced.
# Using re and string is not allowed.
def filter_words(st):
    st = st.split()
    string = ""
    for i in st:
        string += i
        string += " "
    string = list(string)
    string.pop(-1)
    res = ""
    for i in string:
        res += i
    return res.capitalize()


# 4 We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
def number_to_string(num):
    return str(num)


# 5
# You need to write a function that reverses the words in a given string.
# A word can also fit an empty string. If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unnecessary whitespace.
def reverse(st):
    lst = st.split()
    lst_result = []
    print(lst)
    for i in lst:
        print(lst_result)
        lst_result.insert(0, i)
    result = " ".join(lst_result)
    return result


# 6 In this kata you will create a function that takes in a list and returns a list with the reverse order.
def reverse_list(lst):
    return list(reversed(lst))


# 7 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If the number is a multiple of both 3 and 5, only count it once.
def solution(number):
    res = 0
    lst = []
    for i in range(number):
        lst.append(i)
    for i in lst:
        if i % 3 == 0:
            res += i
        elif i % 5 == 0:
            res += i
    return res


# 8 You were camping with your friends far away from home,
# but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False


# 9 Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.
def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


# 10 Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


# 11 Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined
def count_sheep(sheep):
    return sheep.count(True)


# 12 Some new animals have arrived at the zoo.
# The zookeeper is concerned that perhaps the animals do not have the right tails.
# To help her, you must correct the broken function to make sure that the second argument (tail),
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be nonempty strings, and normal letters.
def correct_tail(body, tail):
    if tail == body[-1]:
        return True
    else:
        return False
