print("press 'q|Q' to exit")
 
while True:
    s = input("Choose from next operations:\n"
              " +\n -\n *\n /\n **")
    if s == 'q' or s == "Q":
        break
    if s in ('+', '-', '*', '/', '**'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print("%.2f" % (a + b))
        elif s == '-':
            print("%.2f" (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == '**':
            print("%.2f" % (a**b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("division by zero!")
    else:
        print("invalid input")