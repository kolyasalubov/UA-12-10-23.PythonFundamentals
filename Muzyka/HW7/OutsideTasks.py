#First task
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


print("\nTask1")
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Johnny"))  # Output: Hello, my love!

#Task2


def distance(x1, y1, x2, y2):
    import math
    distance_squared = (x2 - x1)**2 + (y2 - y1)**2
    distance_result = math.sqrt(distance_squared)
    return round(distance_result, 2)


x1, y1 = 1, 2
x2, y2 = 4, 6
print("\nTask2")
print(distance(x1, y1, x2, y2))


#Task3
def filter_words(input_str):
    words = input_str.split()
    if words:
        formatted_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
        return ' '.join(formatted_words)
    else:
        return ''


print("\nTask3")
print(filter_words('HELLO CAN YOU HEAR ME'))
print(filter_words('now THIS is REALLY interesting'))
print(filter_words('THAT was EXTRAORDINARY!'))


#Task4
def number_to_string(num):
    return str(num)


print("\nTask4")
print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))


#Task5

def reverse_words(input_str):
    words = input_str.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words


print("\nTask5")
print(reverse_words("Hello World"))
print(reverse_words("Hi There."))


#Task6
def reverse_list(input_list):
    return list(reversed(input_list))


print("\nTask6")
print(reverse_list([1, 2, 3, 4]))
print(reverse_list([9, 2, 0, 7]))


#Task7
def solution(number):
    if number < 0:
        return 0

    multiples_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples_sum += i

    return multiples_sum


print("\nTask7")
print(solution(10))


#task8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Calculate the maximum distance the car can travel with the remaining fuel
    max_distance = fuel_left * mpg

    # Check if the remaining distance to the pump is less than or equal to the maximum distance
    return distance_to_pump <= max_distance


mpg = 25
distance_to_pump = 50
fuel_left = 2
print("\nTask8")
print(zero_fuel(distance_to_pump, mpg, fuel_left))


#task9
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# Examples
print("\nTask9")
print(are_you_playing_banjo("Rick"))
print(are_you_playing_banjo("Alice"))


#task10
def bool_to_word(boolean_value):
    return "Yes" if boolean_value else "No"


# Examples
print("\nTask10")
print(bool_to_word(True))
print(bool_to_word(False))


#task11
def count_sheeps(sheep_array):
    return sheep_array.count(True)


# Example
sheep_array = [True, True, True, False, True, True, True,
               True, True, False, True, False, True, False,
               False, True, True, True, True, False, False, True, True]
sheep_count = count_sheeps(sheep_array)
print("\nTask11")
print(sheep_count)


#task12
def correct_tail(body, tail):
    return body[-1] == tail


# Example
body_part = "elephant"
tail_part = "t"
result = correct_tail(body_part, tail_part)
print("\nTask12")
print(result)
