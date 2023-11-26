import tkinter as tk
from tkinter import messagebox
import random

HEIGHT = 600
WIDTH = 600
MAX_ATTEMPTS = 10

random_number = random.randint(1, 100)

window = tk.Tk()
window.title("Mysterious Number")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.configure(bg='#3498db')  

attempts_left = MAX_ATTEMPTS

def update_attempts_label():
    attempts_label.config(text=f"Attempts left: {attempts_left}")

def display_result(message):
    messagebox.showinfo("Game Result", message)

def one_click():
    global attempts_left
    if attempts_left > 0:
        choice_user = int(in_value.get()) 
        if choice_user < random_number:
            out_text.config(text="Your number is less than the Mysterious Number", fg="red")
        elif choice_user > random_number:
            out_text.config(text="Your number is greater than the Mysterious Number", fg="red")
        elif choice_user == random_number:
            display_result("Congratulations! You are a winner.")
            window.destroy()
        else:
            out_text.config(text="You are a loser", fg="red")
        
        attempts_left -= 1
        update_attempts_label()
    else:
        display_result("Game over. You've used all your attempts.")
        window.destroy()


in_text = tk.Label(window, text="Enter your number from 1 to 100", font=("Helvetica", 14), bg='#3498db', fg='white')
in_text.pack(pady=10)

attempts_label = tk.Label(window, text=f"Attempts left: {attempts_left}", font=("Helvetica", 14), bg='#3498db', fg='white')
attempts_label.pack()

out_text = tk.Label(window, text="", font=("Helvetica", 14), bg='#3498db', fg='white')
out_text.pack()


in_value = tk.Entry(window, font=("Helvetica", 14))
in_value.pack(pady=10)


button = tk.Button(window, text="GUESS", command=one_click, font=("Helvetica", 16), bg='#2ecc71', fg='white')
button.pack(pady=20)


update_attempts_label()
window.mainloop()
