while True:
    log = input("Enter your login: \t")
    log = log.lower()
    if log == 'first':
        print(f"Welcome {log}")
        break
    else:
        print(f'Error: Uncorrect login. Try another one \n')