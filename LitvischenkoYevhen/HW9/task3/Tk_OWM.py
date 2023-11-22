import tkinter as tk
#from tkinter import font
from OWM import get_weather

HEIGHT = 400
WIDTH = 700

def button_click():
    """Get date fron function weather and print"""
    #clear output
    label.delete(1.0, tk.END)
    #get date
    result = get_weather(entry_field.get())  # Викликайте вашу функцію тут
    #outpup date
    label.insert(tk.END, f"Хмарність          :{result.detailed_status}\n")
    label.insert(tk.END, f"Швидкість вітру    :{result.wind()['speed']}м/с\n")
    label.insert(tk.END, f"Напрямок вітру     :{result.wind()['deg']}\n")
    label.insert(tk.END, f"Вологість          :{result.humidity}%\n")
    label.insert(tk.END, f"Температура повітря:{result.temperature('celsius')['temp']}°C\n")
    label.insert(tk.END, f"Перепад температури:{result.temperature('celsius')['temp_min']} - {result.temperature('celsius')['temp_max']}°C\n")
    label.insert(tk.END, f"Відчувається як    :{result.temperature('celsius')['feels_like']}°C\n")
    label.insert(tk.END, f"Дощь               :{result.rain if result.rain != {} else 'Без дощу'}\n")
    label.insert(tk.END, f"Індекс тепла       :{result.heat_index}\n")
    label.insert(tk.END, f"Хмарність          :{result.clouds}%")

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")

canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="blue", 
                   font=('Courier', 12), 
                   command=button_click)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Text(lower_frame,font=('Courier', 14), bg='green')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

