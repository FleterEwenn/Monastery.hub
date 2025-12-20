from tkinter import *

var = {}

def split_code():
    code = zone_text.get('1.0', END).strip()
    lines = code.split("\n")
    clean_lines = []
    for line in lines:
        if line != "":
            clean_lines.append(line.strip())
    executer_code(clean_lines)

def executer_code(code:list[str]):

    for line in code:
        if line.startswith("spinjutzu"): # affichage dans la console
            pass
        elif line.startswith("nindroide "): # creation d'une variable
            try:
                current_line = line.split("=")
                name = current_line[0][10:]
                val = current_line[1]

                for name in var.keys():
                    if name in val:
                        val = val.split(name)
                        if type(var[name]) == str:
                            tojoin = "'" + var[name] + "'"
                        else:
                            tojoin = str(var[name])
                        
                        val = tojoin.join(val)

                var[name] = eval(val)
            except Exception as e:
                print(e)
            except ValueError as e:
                print(e)
    
    print(var)

window = Tk()

window.title("mini-langage")
window.geometry("800x600")

zone_text = Text(window, width=80, height=20)
execute_btn = Button(window, command=split_code, text="executer")

console = Text(window, width=80, height=13)

execute_btn.pack()
zone_text.pack()

console.pack()
console.config(state=DISABLED)

window.mainloop()