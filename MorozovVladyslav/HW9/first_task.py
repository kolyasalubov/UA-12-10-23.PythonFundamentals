import random


NUMBER = random.randint(0,100)
MAX_ATTEMPTS =10
def run():
    attempts_counter = 0
    win = False

    while attempts_counter<MAX_ATTEMPTS:
        input_ = int(input("Guess number: "))
        if input_ == NUMBER:
            win = True
            
            break
        elif input_< NUMBER:
            print('Bigger number')
        elif input_>NUMBER:
            print('Lower number')
        attempts_counter+=1
    if win:
        print('You win!!!')
    else:
        print('You lost')

if __name__ == '__main__':
    run()
        
