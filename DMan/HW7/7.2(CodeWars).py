#1
def greet(name):

    """greeting Johnny with love, and simply the rest """
    
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return ("Hello, {}!".format(name))


#2    
def distance(x1, y1, x2, y2):

    """
    calculates the distance between two ordered pairs 
    and round it to two decimal places
    """
    
    d=((x2-x1) ** 2 + (y2 - y1) ** 2) 
    return round(d**0.5, 2)


#3
def filter_words(st):

    """filters string capital letter and properly spaces"""
    
    new_st = ' '.join(st.split())
    return new_st.capitalize() 
    #return " ".join(st.capitalize().split())


#4
def numbers_to_text(num):
    
    """transforms a number (integer) into a string"""
    
    return str(num)


#5
def reverseWords(text):

    """reverses the words in a given string"""

    return ' '.join(reversed(text.split()))


#6
def reverse_list(l):

    """reverses list"""

    return l[::-1]
    # return list(reversed(l))


#7

def solution(number):    

    """the sum of all the multiples of 3 or 5 below the number passed in"""

    if number > 0:
        list =[]
        for i in range(number):
            if i%3 == 0 or i%5 == 0:
                list.append(i)
        return sum(list)             
                               
    else:
        return 0  


#8
def zero_fuel(distance_to_pump, mpg, fuel_left):

    """The ability to get a pump, according to the entered data"""

    if distance_to_pump - mpg * fuel_left <= 0:
        return True
    else:
        return False


#9
def are_you_playing_banjo(name):

    """answers the question "Are you playing banjo?" by your name"""
    if name[0] == "r":
        return name +" plays banjo"
    elif name[0] == "R":
        return name +" plays banjo"
    else:
        return name +" does not play banjo"


#10
def bool_to_word(boolean):

    """convert boolean values to strings 'Yes' or 'No'."""

    if boolean == True:
        return "Yes"
    else:
        return "No" 

#11
def count_sheeps(sheep):

    """counts the number of sheep present in the array"""

    # return sum(sheep) - not understood why programm marked this wrong



    total = 0
    for i in sheep:
        if i == True:
            total += i
    return total 


#12
def correct_tail(body, tail):

    """
    confirmation that the second argument, is the same 
    as the last letter of the first argument
    """

    if body[-1] == tail:
        return True
    else:
        return False

