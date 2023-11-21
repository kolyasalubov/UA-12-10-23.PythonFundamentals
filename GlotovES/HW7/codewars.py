######## task 1 #######

'''
Jenny has written a function that returns a greeting for a user. However, 
she's in love with Johnny, and would like to greet him slightly different. 
She added a special case to her function, but she made a mistake.
'''

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {0}!".format(name)

######## task 2 #######

'''
Given two ordered pairs calculate the distance between them. 
Round to two decimal places. This should be easy to do in 0(1) timing.
'''
import math
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)

######## task 3 #######

'''
Write a function taking in a string like WOW this is REALLY          amazing 
and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.
'''
def filter_words(st):
  words = st.split()
  formatted_words = [words[0].capitalize()] + [word.lower()  for word in words[1:]]
  formatted_string = ' '.join(formatted_words)
  return formatted_string

######## task 4 #######

'''
We need a function that can transform a number (integer) into a string.
'''

def number_to_string(num):
    return str(num)

######## task 5 #######

'''
You need to write a function that reverses the words in a given string. 
A word can also fit an empty string. If this is not clear enough, here are some examples:
'''
def reverse(st):
    words = st.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

######## task 6 #######

'''
In this kata you will create a function that takes in a list and returns a list with the reverse order.
'''
def reverse_list(l):
    return l[::-1]

######## task 7 #######

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
'''

def solution(number):
    if number < 0:
        return 0

    sum_multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i

    return sum_multiples


######## task 8 #######

'''
You were camping with your friends far away from home, but when it's time to go back, 
you realize that your fuel is running out and the nearest pump is 50 miles away! 
You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
'''

def zero_fuel(distance_to_pump, mpg, fuel_left):
    dst_on_fuel = fuel_left * mpg
    if dst_on_fuel>=distance_to_pump :
        return True
    else: return False


######## task 9 #######

'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
'''
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    

######## task 10 ####### 

'''
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
'''

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"
    
######## task 11 #######    

'''
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).
'''

def count_sheeps(sheep):
    return sheep.count(True)

######## task 12 ####### 

'''
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. 
To help her, you must correct the broken function to make sure that the second argument (tail), 
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
'''

def correct_tail(body, tail):
     return body[-1] == tail