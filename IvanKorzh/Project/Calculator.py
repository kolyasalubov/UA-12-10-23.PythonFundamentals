import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if len(value) > 23:
        calc.delete(0, tk.END)
        messagebox.showinfo("Warning", "Too many digits")
        calc.insert(0, '0')
        return
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)


def add_operation(operation):
    value = calc.get()
    if len(value) > 23:
        calc.delete(0, tk.END)
        messagebox.showinfo("Warning", "Too many digits")
        calc.insert(0, '0')
        return
    if value[-1] in "+-*/":
        value = value[:-1]
    if '-' in value or '+' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)


def calculate():
    value = calc.get()
    if len(value) > 23:
        calc.delete(0, tk.END)
        messagebox.showinfo("Warning", "Too many digits")
        calc.insert(0, '0')
        return
    if value[-1] in "+-*/":
        value += value[:-1]
    calc.delete(0, tk.END)
    try:
        value = eval(value)
        calc.insert(0, value)
    except (NameError, SyntaxError):
        messagebox.showinfo("Be careful", "Enter only digit!")
        calc.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo("Be careful", "You can't divide by zero")
        calc.insert(0, '0')


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def create_digit_button(digit):
    return tk.Button(window, text=digit, font=('Arial', 18), bd=4, bg='#9F9D9D', command=lambda: add_digit(digit))


def create_calc_button(operation):
    return tk.Button(window, text=operation, font=('Arial', 18), bd=4, bg='#9F9D9D', command=calculate)


def create_operator_button(operator):
    return tk.Button(window, text=operator, font=('Arial', 18), bd=4, fg='green', bg='#9F9D9D',
                     command=lambda: add_operation(operator))


def create_clear_button(operator):
    return tk.Button(window, text=operator, font=('Arial', 18), bd=4, fg='green', bg='#9F9D9D', command=clear)


def press(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


window = tk.Tk()
window.title("Calculator")
window.iconbitmap(default="icon_calc.ico")

window.bind('<Key>', press)

window.minsize(360, 450)
window.maxsize(360, 430)
window.config(bg='black')
calc = tk.Entry(window, justify=tk.RIGHT, font=('Arial', 22), width=10, bg='#9F9D9D')
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='wens', padx=0.2, pady=0.2)

create_digit_button('1').grid(row=1, column=0, stick='wens', padx=0.2, pady=0.2)
create_digit_button('2').grid(row=1, column=1, stick='wens', padx=0.2, pady=0.2)
create_digit_button('3').grid(row=1, column=2, stick='wens', padx=0.2, pady=0.2)
create_digit_button('4').grid(row=2, column=0, stick='wens', padx=0.2, pady=0.2)
create_digit_button('5').grid(row=2, column=1, stick='wens', padx=0.2, pady=0.2)
create_digit_button('6').grid(row=2, column=2, stick='wens', padx=0.2, pady=0.2)
create_digit_button('7').grid(row=3, column=0, stick='wens', padx=0.2, pady=0.2)
create_digit_button('8').grid(row=3, column=1, stick='wens', padx=0.2, pady=0.2)
create_digit_button('9').grid(row=3, column=2, stick='wens', padx=0.2, pady=0.2)
create_digit_button('0').grid(row=4, column=0, stick='wens', padx=0.2, pady=0.2)
create_operator_button('/').grid(row=1, column=3, stick='wens', padx=0.2, pady=0.2)
create_operator_button('+').grid(row=3, column=3, stick='wens', padx=0.2, pady=0.2)
create_operator_button('-').grid(row=2, column=3, stick='wens', padx=0.2, pady=0.2)
create_operator_button('*').grid(row=4, column=3, stick='wens', padx=0.2, pady=0.2)
create_clear_button('C').grid(row=4, column=1, stick='wens', padx=0.2, pady=0.2)
create_calc_button('=').grid(row=4, column=2, stick='wens', padx=0.2, pady=0.2)

window.grid_columnconfigure(0, minsize=90)
window.grid_columnconfigure(1, minsize=90)
window.grid_columnconfigure(2, minsize=90)
window.grid_columnconfigure(3, minsize=90)

window.grid_rowconfigure(0, minsize=90)
window.grid_rowconfigure(1, minsize=90)
window.grid_rowconfigure(2, minsize=90)
window.grid_rowconfigure(3, minsize=90)
window.grid_rowconfigure(4, minsize=90)

window.mainloop()
