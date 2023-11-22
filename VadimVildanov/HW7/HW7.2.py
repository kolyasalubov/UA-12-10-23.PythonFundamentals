"""
1 Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like
to greet him slightly different. She added a special case to her function, but she made a mistake.
Can you help her?
"""


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


"""
2 Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do 
in 0(1) timing.
"""
import math


def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0), 2)


"""
3 Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing.
String should be capitalized and properly spaced. Using re and string is not allowed.
"""


def filter_words(st):
    return " ".join(st.split()).capitalize()


"""
4 We need a function that can transform a number (integer) into a string.
What ways of achieving this do you know?
"""


def number_to_string(num):
    return str(num)