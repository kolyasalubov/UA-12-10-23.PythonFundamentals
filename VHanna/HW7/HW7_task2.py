#1 Jenny's secret message
#Jenny has written a function that returns a greeting for a user. 
#However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
#Can you help her?

def greet(name): 
    if name == "Johnny":
        return "Hello, my love!"
    else: return "Hello, {name}!".format(name=name)

#2 Find The Distance Between Two Points
#Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    x = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    return round(x, 2)

#3 No yelling!
#Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.

def filter_words(st):
    return ' '.join(st.split()).capitalize()

#4 Convert a Number to a String!
#We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know?

def number_to_string(num):
   return str(num)

#5 Reversing Words in a String
#You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:
#As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

def reverse(st):
    s = st.split()
    return ' '.join(s[::-1])