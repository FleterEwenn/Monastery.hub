from tkinter import *

var = {}

def replace_by_values(string:str)->str:
    for name in var.keys():
        if name in string:
            string = string.split(name)
            if type(var[name]) == str:
                tojoin = "'" + var[name] + "'"
            else:
                tojoin = str(var[name])
                    
            string = tojoin.join(string)
    return string

def split_code():
    code = zone_text.get('1.0', END).strip()
    lines = code.split("\n")
    clean_lines = []
    for line in lines:
        if line != "":
            clean_lines.append(line.strip())
    executer_code(clean_lines)

def ecrire_console(text_to_print):
    console.config(state='normal')
    console.insert(END, "\n" + str(text_to_print))
    console.config(state='disabled')

def executer_code(code:list[str]):

    for line in code:
        if line.startswith("spinjutzu "): # affichage dans la console
            current_line = line
            current_text = current_line[10:]

            list_text = current_text.split("'")

            list_string = []

            on_string = False
            string = ""
            for char in current_text:
                if on_string:
                    string += char
                if char == "'":
                    on_string = not on_string
                    list_string.append(string)
                    string = ""
            
            for i in range(len(list_text)):
                if not list_text[i] in list_string:
                    list_text[i] = replace_by_values(list_text[i])                

            #current_text = replace_by_values(current_text)

            ecrire_console(eval(current_text))

        elif line.startswith("nindroide "): # creation d'une variable
            try:
                current_line = line.split("=")
                current_name = current_line[0][9:].strip()
                val = current_line[1]

                val = replace_by_values(val)

                var[current_name] = eval(val)
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