import random

random_number = random.randint(1, 100)
constant_number = random_number
print(random_number)
print("You have only 10 attempts!\n")
attempt = 10
attempt_counter = 0
while attempt_counter < attempt:
     attempt_counter += 1
     print(f"attempt #{attempt_counter}") if attempt_counter < attempt else print(f"attempt #{attempt_counter} (LAST ATTEMPT)")
     user_n = int(input("Guess the number: "))
     if user_n == constant_number:
         print("\nVictory!!!")           
         break
     elif user_n > constant_number:
        print("\nYou lost(") if attempt_counter == 10 else print(f"Your number is bigger on {user_n - constant_number}\n")
     elif user_n < constant_number:
        print("\nYou lost(") if attempt_counter == 10 else print(f"Your number is less on {constant_number - user_n}\n")
   