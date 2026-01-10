from tkinter import *

var = {}
list_if_codes = []

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

    if_code = []
    on_if = False

    for line in lines:

        if on_if:
            if_code.append(line.strip())
        
        if line != "" and not on_if:
            clean_lines.append(line.strip())

        if line != "" and line.strip()[-1] == "{":
            on_if = True
        if line != "" and line.strip()[-1] == "}":
            on_if = False
            list_if_codes.append(if_code)
            if_code = []

    executer_code(clean_lines)

def ecrire_console(text_to_print):
    console.config(state='normal')
    console.insert(END, "\n" + str(text_to_print))
    console.config(state='disabled')

def executer_code(code:list[str]):

    for line in code:
        print(line)
        if line.startswith("spinjutzu "): # affichage dans la console
            try:
                current_line = line
                current_text = current_line[10:]

                list_text = current_text.split("'")
                if len(list_text)%2 == 0:
                    raise SyntaxError(f"syntaxe invalide, ligne {code.index(line) + 1} : la chaine de caractère est mal delimitée")

                list_string = []

                on_string = False
                string = ""
                for char in current_text:
                    if on_string:
                        string += char
                    if char == "'":
                        if on_string:
                            list_string.append(string[:-1])
                        string = ""
                        on_string = not on_string
                
                for i in range(len(list_text)):
                    if list_text[i] in list_string:
                        list_text[i] = "'" + list_text[i] + "'"
                    else:
                        list_text[i] = replace_by_values(list_text[i])
                
                current_text = "".join(list_text)

                ecrire_console(eval(current_text))
            
            except NameError as e:
                name = ""
                on_name = False
                for char in str(e):
                    if on_name:
                        name += char
                    if char == "'":
                        on_name = not on_name
                ecrire_console(f"la variable '{name[:-1]}' n'est pas definie, ligne {list_line.index(line) + 1}")
            except Exception as e:
                ecrire_console(e)

        elif line.startswith("nindroide "): # creation d'une variable
            try:
                current_line = line.split("=")
                current_name = current_line[0][9:].strip()
                val = current_line[1]

                list_text = val.split("'")
                if len(list_text)%2 == 0:
                    raise SyntaxError(f"syntaxe invalide, ligne {code.index(line) + 1} : la chaine de caractère est mal delimitée")

                list_string = []

                on_string = False
                string = ""
                for char in val:
                    if on_string:
                        string += char
                    if char == "'":
                        if on_string:
                            list_string.append(string[:-1])
                        on_string = not on_string
                        string = ""
                
                for i in range(len(list_text)):
                    if list_text[i] in list_string:
                        list_text[i] = "'" + list_text[i] + "'"
                    else:
                        list_text[i] = replace_by_values(list_text[i])
                
                val = "".join(list_text)

                var[current_name] = eval(val)

            except NameError as e:
                name = ""
                print(e)
                on_name = False
                for char in str(e):
                    if on_name:
                        name += char
                    if char == "'":
                        on_name = not on_name

                ecrire_console(f"la variable '{name[:-1]}' n'est pas definie, ligne {code.index(line) + 1}")
            except Exception as e:
                ecrire_console(e)

        elif line.startswith("wu "): # if
            list_line = line.split("{")
            bool_ = list_line[0][2:-1]

            list_text = bool_.split("'")
            if len(list_text)%2 == 0:
                raise SyntaxError(f"syntaxe invalide, ligne {code.index(line) + 1} : la chaine de caractère est mal delimitée")

            list_string = []

            on_string = False
            string = ""
            for char in bool_:
                if on_string:
                    string += char
                if char == "'":
                    if on_string:
                        list_string.append(string[:-1])
                    string = ""
                    on_string = not on_string
                
            for i in range(len(list_text)):
                if list_text[i] in list_string:
                    list_text[i] = "'" + list_text[i] + "'"
                else:
                    list_text[i] = replace_by_values(list_text[i])
                
            bool_ = "".join(list_text)
            bool_ = eval(bool_)

            if bool_:
                executer_code(list_if_codes[0])
                list_if_codes.pop(0)

        elif line != "}":
            ecrire_console(f"la commande n'existe pas, ligne {code.index(line) + 1}")
        
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