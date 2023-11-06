login = ""
while True :
   login = input("Enter your username: ")
   if login == "First":
      print(f"Hello, {login}!")
      break
   else:
      print("Eror: Incorrect login \nTry again")
      continue
      