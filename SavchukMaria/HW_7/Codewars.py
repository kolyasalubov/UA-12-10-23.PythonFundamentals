#task 1
#Jenny has written a function that returns a greeting for a user.
#However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
#Can you help her?

def greet(name):
  if name == "Johnny":
      return "Hello, my love!"
      return "Hello, {name}!".format(name=name)

#task2
#Given two ordered pairs calculate the distance between them. Round to two decimal places.
#This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    import math
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)


#task3
#Write a function taking in a string like WOW this is REALLY amazing and
#returning Wow this is really amazing.
#String should be capitalized and properly spaced. Using re and string is not allowed.

def filter_words(input_str):
    words = input_str.split()
    if words:
        formatted_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
        return ' '.join(formatted_words)
    else:
        return ''



# task 4
#We need a function that can transform a number (integer) into a string

def number_to_string(num):
    return str(num)

#Task5
#You need to write a function that reverses the words in a given string.

def reverse(st):
    words = st.strip().split()
    words.reverse()
    return ' '.join(words)

#Task6
#In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(input_list):
    return list(reversed(input_list))

#Task7
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.


def solution(number):
    if number < 0:
        return 0

    multiples_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples_sum += i

    return multiples_sum

#Task8
#You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
#Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = fuel_left * mpg

    return distance_to_pump <= max_distance

#Task9
#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#Task10
#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false. """
def bool_to_word(bool):
    return "Yes" if bool else "No"

#Task11
#Consider an array/list of sheep where some sheep may be missing from their place.
#We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep_array):
    return sheep_array.count(True)

#Task12
#ome new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
#If the tail is right return true, else return false.
#The arguments will always be non empty strings, and normal letters.

def correct_tail(body, tail):
    return body[-1] == tail