from random import randint
from tkinter import *
#count_attempt = 10

def more_less():
    """check number and show message"""
    global count_attempt
    count_attempt -= 1
    info['text'] = f'You have {count_attempt} attempts left'
    ask_number = int(inputNumber.get())
    if gues_number < ask_number :
        title['text'] = 'Guess number less then your chois'
    elif gues_number > ask_number:
        title['text'] = 'Guess number greater then your chois'
    else:
        title['text'] = (f'***********You Won!!!***********')
        title['bg'] = 'green'
    if count_attempt == 0 :
        title['text'] = ('*************You loose***********')
        title['bg'] = 'red'

def try_again():
    """clear frame and arguments"""
    global gues_number 
    gues_number = randint(1, 100)
    global count_attempt
    count_attempt = 10
    title['bg'] = 'lightgrey'
    title['text'] = 'Guess tne number from 1 to 100'
    info['text'] = f'You have {count_attempt} attempts left'
    inputNumber.delete(0, len(inputNumber.get()) )    

#generate number    
#gues_number = randint(1, 100)
#create window
window = Tk()
window.title('Gues number?')
window.geometry('350x200')
window.resizable(width=False, height=False)
#create frame
frame = Frame(window, bg='grey')
frame.place(relwidth=0.8, relheight=0.8, relx= 0.1, rely=0.1)

title = Label(frame, text='Guess tne number from 1 to 100', bg='lightgrey', font=14)
title.place(relx=0.1, rely=0.1)
inputNumber = Entry(frame, bg='white')
inputNumber.place(relx=0.27, rely=0.3)
btn = Button(frame, text='Check the number', command=more_less)
btn.place(relx=0.3, rely=0.5)
info = Label(frame, text='You have 10 attempts left', bg='grey')
info.place(relx=0.2, rely=0.7)
#button for clear program and start again
btnTry = Button(frame, text='Try again', command=try_again)
btnTry.place(relx=0.01, rely=0.83)

#init arguments
try_again()

mainloop()

