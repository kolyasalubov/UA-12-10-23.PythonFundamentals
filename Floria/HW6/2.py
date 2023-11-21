while True :
   login = input("Enter your username: ")
   if login == "First":
      print(f"Hello, {login}!")
      break
   else:
      print("Incorrect login. Please try again.")
      continue