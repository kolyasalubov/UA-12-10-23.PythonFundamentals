from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# БЛОК Ф-Й ДЯЛ File
def close_note():
    answer = messagebox.askokcancel("Exit", "Do you want to close app?")
    if answer:
        window.destroy()

def open_file():
    file_path = filedialog.askopenfilename(title="Choose a file", filetypes=(("Text  documents(*.txt)", "*.txt"), ("All files", "*.*")))
    if file_path:
        text_field.delete("1.0", END)
        text_field.insert("1.0", open(file_path, encoding="utf-8").read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("Text  documents(*.txt)", "*.txt"), ("All files", "*.*")))
    f = open(file_path, "w", encoding="utf-8")
    text = text_field.get("1.0", END)
    f.write(text)
    f.close()


# БЛОК Ф-Й ДЯЛ View\Theme\Font-Type\Font-Style\Font-Size
def switch_theme(theme):
    text_field["bg"] = view_theme[theme]["text_bg"]
    text_field["fg"] = view_theme[theme]["text_fg"]
    text_field["insertbackground"] = view_theme[theme]["cursor"]
    text_field["selectbackground"] = view_theme[theme]["select_bg"]

def switch_fonts_type(fonttype):
    global font_type
    font_type = view_font_type[fonttype]["font_tp"]
    update_text_font()

def switch_fonts_style(fontstyle):
    global font_style
    font_style = view_font_style[fontstyle]["font_st"]
    update_text_font()

def switch_fonts_size(fontsize):
    global font_size
    font_size = view_fonts_size[fontsize]["font_sz"]
    update_text_font()

def update_text_font():
    text_field.config(font=(font_type, font_size, font_style))


window = Tk()
window.title("Notepad")
window.iconbitmap("icons\TkNotepad.ico")
window.geometry("500x600")

main_menu = Menu(window)  # оголошуємо віджет МЕНЮ
file_menu = Menu(main_menu, tearoff=0)
view_menu = Menu(main_menu, tearoff=0)  # оголошуємо ОСНОВНЕ1 випадаюче меню в МЕНЮ

main_menu.add_cascade(label="File", menu=file_menu)  # КАСКАД ДЛЯ ВСІХ КАСКАДІВ В НЬОМУ
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_note)
window.config(menu=file_menu) 

main_menu.add_cascade(label="View", menu=view_menu) # КАСКАД ДЛЯ ВСІХ КАСКАДІВ В НЬОМУ
theme_menu_sub = Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Theme", menu=theme_menu_sub)
theme_menu_sub.add_command(label="Deffault", command=lambda: switch_theme("deffault"))
theme_menu_sub.add_command(label="Dark", command=lambda: switch_theme("dark"))
theme_menu_sub.add_command(label="Fallout-Terminal", command=lambda: switch_theme("fallout_terminal"))
theme_menu_sub.add_command(label="Dracula", command=lambda: switch_theme("dracula"))

font_type_menu_sub = Menu(view_menu, tearoff=0) #  оголошуємо випадаюче меню(1) в ОСНОВНОМУ каскаді
view_menu.add_cascade(label="Font-Type", menu=font_type_menu_sub) #  каскад font_style_menu_sub 
font_type_menu_sub.add_command(label="Arial", command=lambda: switch_fonts_type("arial")) # параметр в каскаді  font_style_menu_sub 
font_type_menu_sub.add_command(label="Comic Sans MS", command=lambda: switch_fonts_type("comic_sans_ms")) # параметр в каскаді  font_style_menu_sub 
font_type_menu_sub.add_command(label="Times New Roman", command=lambda: switch_fonts_type("times_new_roman")) # параметр в каскаді  font_style_menu_sub 

font_style_menu_sub =  Menu(view_menu, tearoff=0) # оголошуємо випадаюче меню(3) в ОСНОВНОМУ каскаді
view_menu.add_cascade(label="Font-Style", menu=font_style_menu_sub)
font_style_menu_sub.add_command(label="Deffault", command=lambda: switch_fonts_style("deffault"))
font_style_menu_sub.add_command(label="Bold", command=lambda: switch_fonts_style("bold"))
font_style_menu_sub.add_command(label="Italc", command=lambda: switch_fonts_style("italic"))

font_size_menu_sub =  Menu(main_menu, tearoff=0) # оголошуємо випадаюче меню(3) в ОСНОВНОМУ каскаді
view_menu.add_cascade(label="Size", menu=font_size_menu_sub) # каскад font_size_menu_sub 
font_size_menu_sub.add_command(label="50%", command=lambda: switch_fonts_size("50")) # параметр в каскаді  font_size_menu_sub
font_size_menu_sub.add_command(label="100% (Deffault)", command=lambda: switch_fonts_size("100")) # параметр в каскаді  font_size_menu_sub
font_size_menu_sub.add_command(label="150%", command=lambda: switch_fonts_size("150")) # параметр в каскаді  font_size_menu_sub
font_size_menu_sub.add_command(label="200%", command=lambda: switch_fonts_size("200")) # параметр в каскаді  font_size_menu_sub
font_size_menu_sub.add_command(label="250%", command=lambda: switch_fonts_size("250")) # параметр в каскаді  font_size_menu_sub

window.config(menu=main_menu) # відображення всього доданого 


frame_text = Frame(window)
frame_text.pack(fill=BOTH, expand=1)

view_theme = {
    "deffault":{
        "text_bg": "white",
        "text_fg": "black",
        "cursor": "black",
        "select_bg": "blue"
    },
    
    "dark":{
        "text_bg": "black",
        "text_fg": "white",
        "cursor": "white",
        "select_bg": "gray"
    },
    
    "fallout_terminal":{
        "text_bg": "black",
        "text_fg": "green",
        "cursor": "green",
        "select_bg": "lime"
    },
    
    "dracula":{
        "text_bg": "purple",
        "text_fg": "violet",
        "cursor": "yellow",
        "select_bg": "turquoise"
    }
}


view_font_type = {
    "arial": {"font_tp": "Arial"},
    "comic_sans_ms": {"font_tp": "Comic Sans MS"},
    "times_new_roman": {"font_tp": "Times New Roman"}
}

view_font_style = {
    "deffault": {"font_st": ""},
    "italic": {"font_st": "italic"},
    "bold": {"font_st": "bold"}
}

view_fonts_size = {
    "50": {"font_sz": 8},
    "100": {"font_sz": 16},
    "150": {"font_sz": 24},
    "200": {"font_sz": 32},
    "250": {"font_sz": 40}
}

font_type = "Arial"
font_style = ""
font_size = 16

text_field = Text(frame_text,
                  bg="white",
                  fg="black",
                  font=(font_type, font_size, font_style),
                  padx=10,
                  pady=10,
                  wrap=WORD,
                  insertbackground="black",
                  selectbackground="blue",
                  spacing3=5,
                  width=30)
text_field.pack(fill=BOTH, expand=1, side=LEFT)

scroll_line = Scrollbar(frame_text, command=text_field.yview)
scroll_line.pack(expand=1, fill=Y)
text_field.config(yscrollcommand=scroll_line.set)

window.mainloop()