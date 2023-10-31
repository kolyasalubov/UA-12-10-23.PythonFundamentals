even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []

for num in range(1, 11):
    if num % 2 == 0:
        even_divisible_by_2.append(num)
    if num % 2 == 1 and num % 3 == 0:
        odd_divisible_by_3.append(num)
    if num % 2 != 0 and num % 3 != 0:
        not_divisible_by_2_or_3.append(num)

# Print the results
print("Even numbers divisible by 2:", even_divisible_by_2)
print("Odd numbers divisible by 3:", odd_divisible_by_3)
print("Numbers not divisible by 2 and 3:", not_divisible_by_2_or_3)


expected_login = "Kolia"

# Prompt the user to enter a login
user_login = input("Enter your login: ")

# Check the login using a while loop
while user_login != expected_login:
    print("Error! Login is different.")
    user_login = input("Enter your login: ")

# Greet the user when the correct login is entered
print("Hello, user!")
