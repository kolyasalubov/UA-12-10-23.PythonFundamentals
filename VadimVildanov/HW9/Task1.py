import random
import math

lower = 1
upper = 100

# generating random number between the lower and upper
x = random.randint(lower, upper)
print("You've only ", round(10), " chances to guess the integer!")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number: "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ", count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses, shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("The number is %d" % x)
	print("Better Luck Next time!")




