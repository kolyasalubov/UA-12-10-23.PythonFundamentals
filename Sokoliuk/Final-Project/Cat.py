from tkinter import *
from tkinter import messagebox as mb
import time
import random
import pandas as pd
import os

events = pd.read_csv(os.path.abspath("Events.csv"))

class Tkinter(Tk):
    
    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="lightblue")
        self.win.geometry("450x500")
        self.win.title("Cat trainer")
        self.win.resizable(False, False)

        self.icon = PhotoImage(file=os.path.abspath("iconCat.png"))
        self.win.iconphoto(True, self.icon)

        self.logo = PhotoImage(file=os.path.abspath("cat.png"))
        self.logo1 = Label(image=self.logo)

        self.healthCat = 20
        self.leisureCat = 20
        self.disciplineCat = 20
        self.trustCat = 20
        self.max_value = 150

        self.click_flag = False
        self.event_flag = True

        self.start_time = None
        self.name = "Cat"

        self.var = StringVar()
        self.max_len = 12

        # Initialize main elements of the game

        self.label_title = Label(bg="lightblue",width=27, height=3, text=f"This is your {self.name}",font=("Arial", 12))
        self.label_info = Label(bg="lightblue",justify="center",width=20,height=3,text=None,font=("Arial", 12))
        self.b1 = Button(width=15,text="feed",command=self.health)
        self.b2 = Button(width=15,text="play",command=self.leisure)
        self.b3 = Button(width=15,text="train",command=self.discipline)
        self.b4 = Button(width=15,text="caress",command=self.trust)
        self.b5 = Button(width=15,text="Exit",command=quit)
        self.l1 = Label(bg="lightblue",anchor="w",width=20,height=2,text="health - " + str(self.healthCat) + "%")
        self.l2 = Label(bg="lightblue",anchor="w",width=20,height=2,text="leisure - " + str(self.leisureCat) + "%")
        self.l3 = Label(bg="lightblue",anchor="w",width=20,height=2,text="discipline - " + str(self.disciplineCat) + "%")
        self.l4 = Label(bg="lightblue",anchor="w",width=20,height=2,text="trust - " + str(self.trustCat) + "%")
        self.l5 = Label(bg="lightblue",width=20,height=2,text=f"your {self.name} is alive")
        self.label_delimiter = Label(bg="lightblue",anchor="w",width=50,height=1,text="==================================================", font=12)
        self.label_event_info = Label(bg="lightblue",justify="center",anchor="n",width=40,height=5,text=None,font=("Arial", 14))

        # Initialize hidden elements of the main game

        hidden_elements = [self.label_title, self.label_info, self.b1, self.b2,
                        self.b3, self.b4, self.b5, self.l1, self.l2, self.l3,
                        self.l4, self.l5, self.logo1, self.label_delimiter]

        for element in hidden_elements:
            element = element.grid_forget()

        # Initialize initial elements of the game (will be destroyed after button click)

        self.entry_field = Entry(justify="center", font=("Tahoma", 12), textvariable=self.var)
        self.button_for_name = Button(bg="orange",text="Name", command=self.get_name)
        self.label_for_name = Label(bg="lightblue",text="Name your Cat")
        self.label_for_name.place(x=80, y=25, width=100, height=30)
        self.entry_field.place(x=80, y=70, width=100, height=30)
        self.button_for_name.place(x=250, y=40, width=100, height=60)

        self.var.trace_add("write", self.entry_restriction)

        self.win.mainloop()

    def entry_restriction(self,*args):
        """Create restriction to the amount of characters (for Entry widget)"""
        string = self.var.get()
        if len(string) > self.max_len:
            self.var.set(string[:self.max_len])

    def get_event(self,df):
        """Gets random event from the dataframe and change values accrodingly"""
        event_number = random.randint(0,9)
        self.label_event_info.configure(text=df.at[event_number, "text"])
        if self.healthCat + df.at[event_number, "health"] >= self.max_value:
            self.healthCat = self.max_value
        else:
            self.healthCat += df.at[event_number, "health"]
        if self.leisureCat + df.at[event_number, "leisure"] >= self.max_value:
            self.leisureCat = self.max_value
        else:
            self.leisureCat += df.at[event_number, "leisure"]
        if self.disciplineCat + df.at[event_number, "discipline"] >= self.max_value:
            self.disciplineCat = self.max_value
        else:
            self.disciplineCat += df.at[event_number, "discipline"]
        if self.trustCat + df.at[event_number, "trust"] >= self.max_value:
            self.trustCat = self.max_value
        else:   
            self.trustCat += df.at[event_number, "trust"]
        self.l1.configure(text="health - " + str(self.healthCat) + "%")
        self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
        self.l3.configure(text="discipline - " + str(self.disciplineCat) + "%")
        self.l4.configure(text="trust - " + str(self.trustCat) + "%")

    def update_event(self):
        """Recursive call for get_event function"""
        if self.event_flag:
            self.get_event(events)
            self.win.after(4000, self.update_event)

    def check_stats(self):
        """Checks the stats of the pet, control buttons for actions and quit the game if answer is False"""
        end_time = time.time()
        if self.healthCat <= 0 or self.leisureCat <= 0 or self.disciplineCat <= 0 or self.trustCat <= 0:
            self.event_flag = False
            answer = mb.askyesno(title="You lost", message="Do you want to play again?")
            if answer == True:
                self.healthCat = 20
                self.leisureCat = 20
                self.disciplineCat = 20
                self.trustCat = 20
                self.l1.configure(text="health - " + str(self.healthCat) + "%")
                self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
                self.l3.configure(text="discipline - " + str(self.disciplineCat) + "%")
                self.l4.configure(text="trust - " + str(self.trustCat) + "%")
                self.event_flag = True
            else:
                result_time = end_time - self.start_time
                result_time = time.strftime("%H:%M:%S", time.gmtime(result_time))
                mb.showinfo(message=f"Goodbye!, you spent {result_time} time with your pet")
                self.win.quit()
        elif self.healthCat >= 100 and self.leisureCat >= 100 and self.disciplineCat >= 100 and self.trustCat >= 100:
            self.event_flag = False
            answer = mb.askyesno(title="you win", message="Do you want to play again?")
            if answer == True:
                self.healthCat = 20
                self.leisureCat = 20
                self.disciplineCat = 20
                self.trustCat = 20
                self.l1.configure(text="health - " + str(self.healthCat) + "%")
                self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
                self.l3.configure(text="discipline - " + str(self.disciplineCat) + "%")
                self.l4.configure(text="trust - " + str(self.trustCat) + "%")
                self.event_flag = True
            else:
                result_time = end_time - self.start_time
                result_time = time.strftime("%H:%M:%S", time.gmtime(result_time))
                mb.showinfo(message=f"Goodbye!, you spent {result_time} time with your pet")
                self.win.quit()
        
        if self.healthCat <= 10:
            self.label_info.configure(text=f"Attention!\n{self.name}\nis hungry")
        else:
            self.label_info.configure(text=f"{self.name}\nis sated")

    def update_gui(self):
        """Recursive call for check_stats function"""
        self.check_stats()
        self.win.after(1000, self.update_gui)

    def health(self):
        """Changes the health value and updates info"""
        if self.healthCat + 10 >= self.max_value:
            self.healthCat = self.max_value
        else:
            self.healthCat += 10
        self.leisureCat -= 0
        self.disciplineCat -= 1
        self.trustCat += 2
        self.l1.configure(text="health - " + str(self.healthCat) + "%")
        self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
        self.l3.configure(text="discipline - " + str(self.disciplineCat) + "%")
        self.l4.configure(text="trust - " + str(self.trustCat) + "%")
        self.l5.configure(text=f"You fed {self.name}")
        self.click_flag = True
        self.click_block()

    def leisure(self):
        """Changes the leisure value and updates info"""
        if self.healthCat <= 10:
            pass
        else:
            if self.leisureCat + 10 >= self.max_value:
                self.leisureCat = self.max_value
            else:
                self.leisureCat += 10
            self.healthCat -= 2
            self.disciplineCat -= 2
            self.trustCat += 1
            self.l1.configure(text="health - " + str(self.healthCat) + "%")
            self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
            self.l3.configure(text="discipline - " + str(self.disciplineCat) + "%")
            self.l4.configure(text="trust - " + str(self.trustCat) + "%")
            self.l5.configure(text=f"You played with {self.name}")
            self.click_flag = True
            self.click_block()

    def discipline(self):
        """Changes the discipline value and updates info"""
        if self.healthCat <= 10:
            pass
        else:
            if self.disciplineCat + 10 >= self.max_value:
                self.disciplineCat = self.max_value
            else:
                self.disciplineCat += 10
            self.healthCat -= 5
            self.leisureCat -= 3
            self.trustCat -= 0
            self.l1.configure(text="health - " + str(self.healthCat) + "%")
            self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
            self.l3.configure(text="discipline - " + str(self.disciplineCat) + "%")
            self.l4.configure(text="trust - " + str(self.trustCat) + "%")
            self.l5.configure(text=f"You trained {self.name}")
            self.click_flag = True
            self.click_block()

    def trust(self):
        """Changes the trust value and updates info"""
        if self.healthCat <= 10:
            pass
        else:
            if self.trustCat + 10 >= self.max_value:
                self.trustCat = self.max_value
            else:
                self.trustCat += 10
            self.healthCat -= 3
            self.leisureCat += 1
            self.disciplineCat -= 2
            self.l1.configure(text="health - " + str(self.healthCat) + "%")
            self.l2.configure(text="leisure - " + str(self.leisureCat) + "%")
            self.l3.configure(text="discipline - " + str(self.disciplineCat) + "%")
            self.l4.configure(text="trust - " + str(self.trustCat) + "%")
            self.l5.configure(text=f"You caressed {self.name}")
            self.click_flag = True
            self.click_block()

    def click_block(self):
        """Disables buttons for 1 second to prevent spam"""
        if self.click_flag:
            self.b1.configure(state="disabled")
            self.b2.configure(state="disabled")
            self.b3.configure(state="disabled")
            self.b4.configure(state="disabled")
            self.win.after(1000, self.click_allow)

    def click_allow(self):
        """Enables buttons after blocking"""
        self.b1.configure(state="normal")
        self.b2.configure(state="normal")
        self.b3.configure(state="normal")
        self.b4.configure(state="normal")
        self.click_flag = False

    def get_name(self):
        """Get the name from Entry element, then delete previous elements and display the main game"""
        if self.entry_field.get() == "":
            self.name = "Cat"
        else:
            self.name = self.entry_field.get()
        self.start_time = time.time()
        self.entry_field.destroy()
        self.button_for_name.destroy()
        self.label_for_name.destroy()
        self.label_title.configure(text=f"This is your {self.name}",font="Arial")
        self.l5.configure(text=f"your {self.name} is alive")
        self.label_title.place(x=135, y=5)
        self.label_info.place(x=-10, y=10)
        self.b1.place(x=25, y=80)
        self.b2.place(x=25, y=120)
        self.b3.place(x=25, y=160)
        self.b4.place(x=25, y=200)
        self.b5.place(x=240, y=320)
        self.l1.place(x=25, y=250)
        self.l2.place(x=25, y=280)
        self.l3.place(x=25, y=310)
        self.l4.place(x=25, y=340)
        self.l5.place(x=225, y=270)
        self.logo1.place(x=225, y=70)
        self.label_delimiter.place(x=0,y=380)
        self.label_event_info.place(x=0, y=410)
        self.update_gui()
        self.update_event()

if __name__ == "__main__":
    game = Tkinter()
