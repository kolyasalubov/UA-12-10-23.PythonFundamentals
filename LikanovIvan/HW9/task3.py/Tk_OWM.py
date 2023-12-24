import tkinter as tk
from OWM import get_weather

HEIGHT = 500
WIDTH = 700


def click():
    label.delete('1.0', tk.END)
    result = get_weather(entry_field.get())
    label.insert(tk.END, f"In {entry_field.get()} is {result.detailed_status}\n")
    label.insert(tk.END, f"Wind speed:{result.wind()['speed']} meters per second\n")
    label.insert(tk.END, f"Humidity:{result.humidity}%\n")
    label.insert(tk.END, f"Temperature:{round(result.temperature('celsius')['temp'])}\n")
    label.insert(tk.END, f"Maximum temperature:{round(result.temperature('celsius')['temp_max'])}\n")
    label.insert(tk.END, f"Minimum temperature:{round(result.temperature('celsius')['temp_min'])}\n")
    label.insert(tk.END, f"Heat index:{result.heat_index}\n")


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
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=click)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Text(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
