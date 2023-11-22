#task1
# Create a function that returns the mean of all digits.
# The mean of all digits is the sum of digits / how many 
# digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=3).
# The mean will always be an integer.

# def mean(num):
#     num_str = str(num)
#     non_zero_digits = [int(digit) for digit in num_str if digit != '0']
    
#     if non_zero_digits:
#         mean_value = sum(non_zero_digits) / len(non_zero_digits)
#     else:
#         mean_value = 0
    
#     return int(mean_value)

#task2
# Create a function which returns a list of booleans, from a given number. 
# Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.
# Notes. Expect numbers with 0 and 1 only.

# def integer_boolean(binary_number):
#     binary_str = str(binary_number)
#     boolean_list = []
#     for digit in binary_str:
#         boolean_list.append(True if digit == '1' else False)
#     return boolean_list

#task3
# An isogram is a word that has no duplicate letters. Create a function that takes a string 
# and returns either True or False depending on whether or not it's an "isogram".
# Notes.
#     Ignore letter case (should not be case sensitive).
#     All test cases contain valid one word strings.

# def is_isogram(word):
#     word = word.lower()
#     letter_set = set()
#     for letter in word:
#         if letter in letter_set:
#             return False
#     else: 
#         letter_set.add(letter)
#     return True

#task4
# Create a function that takes a string and returns 
# the number (count) of vowels contained within it.
# Notes
#     a, e, i, o, u are considered vowels (not y).
#     All test cases are one word and only contain letters.

# def count_vowels(word):
#     vowels = set("aeiou")
#     word = word.lower()
#     vowel_count = 0
#     for letter in word:
#         if letter in vowels:
#             vowel_count += 1
#     return vowel_count

#task5
# Create a function that returns a base-2 (binary) representation of a 
# base-10 (decimal) string number. To convert is simple: ((2) means base-2 and 
# (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
# Going from right to left, the value of the most right bit is 1, now 
# from that every bit to the left will be x2 the value, value of an 8 bit 
# binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
# Notes
# Numbers will always be below 1024 (not including 1024).
# The strings will always go to the length at which the most 
# left bit's value gets bigger than the number in decimal.
# If a binary conversion for 0 is attempted, return "0".

# def binary(decimal):
#     decimal = int(decimal)
    
#     if decimal == 0:
#         return "0"
    
#     binary_digits = []
    
#     while decimal > 0:
#         remainder = decimal % 2
#         binary_digits.insert(0, str(remainder))
#         decimal //= 2
    
#     binary_string = "".join(binary_digits)
#     return binary_string
