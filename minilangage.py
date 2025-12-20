from tkinter import *

def split_code():
    code = zone_text.get('1.0', END).strip()
    lines = code.split("\n")
    clean_lines = []
    for line in lines:
        if line != "":
            clean_lines.append(line.strip())
    executer_code(clean_lines)

def executer_code(code:list):
    print(code)

window = Tk()

window.title("mini-langage")
window.geometry("800x600")

zone_text = Text(window, width=80, height=20)
execute_btn = Button(window, command=split_code, text="executer")

execute_btn.pack()
zone_text.pack()

window.mainloop()