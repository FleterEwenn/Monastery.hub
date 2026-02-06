#Projet : monastery.hub
#Auteurs : Ewenn Fleter, Raphael Kermes

from tkinter import *

var = {}
list_if_codes = []

def trifusion(list_:list)->list:
    n = len(list_)
    c = n//2

    if n <= 1:
        return list_
    
    else:
        list1 = trifusion(list_[:c])
        list2 = trifusion(list_[c:])
        return fusionner(list1, list2)

def fusionner(list1:list, list2:list)->list:
    if list2 == []:
        return list1
    if list1 == []:
        return list2
    
    if len(list1[0]) > len(list2[0]):
        return [list1[0]] + fusionner(list1[1:], list2)
    else:
        return [list2[0]] + fusionner(list1, list2[1:])


def replace_by_values(string:str)->str:
    list_name = trifusion(list(var.keys()))
    for name in list_name:
        if name in string:
            string = string.split(name)
            if type(var[name]) == str:
                tojoin = "'" + var[name] + "'"
            else:
                tojoin = str(var[name])
                    
            string = tojoin.join(string)
    return string

def split_code():
    global nbr_line
    nbr_line = 0
    code = zone_text.get('1.0', END).strip()
    lines = code.split("\n")
    clean_lines = []

    nbr_if = 0

    if_code = []
    on_if = False

    for line in lines:

        if on_if:
            if_code.append(line.strip())
        
        if not on_if:
            clean_lines.append(line.strip())

        if line != "" and line.strip()[-1] == "{":
            nbr_if += 1
            on_if = True
        if line != "" and line.strip()[-1] == "}":
            nbr_if -= 1
            on_if = False
            list_if_codes.append(if_code)
            if_code = []

    ecrire_console("")
    if nbr_if != 0:
        ecrire_console("erreur de syntaxe : '{' ou '}' a été utilisé à tort")
    else:
        executer_code(clean_lines)

def ecrire_console(text_to_print, pre=''):
    console.config(state='normal')
    console.insert(END, "\n" + pre + str(text_to_print))
    console.config(state='disabled')

def executer_code(code:list[str]):
    global nbr_line

    for line in code:
        nbr_line += 1

        if line[-1] == "}":
            line = line[:-1]

        if line.startswith("spinjutzu "): # affichage dans la console
            try:
                current_line = line
                current_text = current_line[10:]

                list_text = current_text.split("'")
                if len(list_text)%2 == 0:
                    raise SyntaxError(f"syntaxe invalide, ligne {nbr_line} : la chaine de caractère est mal delimitée")

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

                ecrire_console(eval(current_text), pre='>> ')
            
            except NameError as e:
                name = ""
                on_name = False
                for char in str(e):
                    if on_name:
                        name += char
                    if char == "'":
                        on_name = not on_name
                ecrire_console(f"la variable '{name[:-1]}' n'est pas definie, ligne {nbr_line}")
            except Exception as e:
                ecrire_console(e)

        elif line.startswith("nindroide "): # creation/modification de variable
            try:
                current_line = line.split("=")
                current_name = current_line[0][9:].strip()
                val = current_line[1]

                list_text = val.split("'")
                if len(list_text)%2 == 0:
                    raise SyntaxError(f"syntaxe invalide, ligne {nbr_line} : la chaine de caractère est mal delimitée")

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
                on_name = False
                for char in str(e):
                    if on_name:
                        name += char
                    if char == "'":
                        on_name = not on_name

                ecrire_console(f"la variable '{name[:-1]}' n'est pas definie, ligne {nbr_line}")
            except SyntaxError as e:
                if str(e).startswith("'{' was never closed"):
                    ecrire_console(f"erreur de syntaxe, ligne {nbr_line} :" + " '{' a été utilisé à tort")
                else:
                    ecrire_console(e)
            except Exception as e:
                ecrire_console(e)

        elif line.startswith("wu "): # if
            try:
                list_line = line.split("{")
                bool_ = list_line[0][2:-1]

                list_text = bool_.split("'")
                if len(list_text)%2 == 0:
                    raise SyntaxError(f"syntaxe invalide, ligne {nbr_line} : la chaine de caractère est mal delimitée")

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
            except NameError as e:
                name = ""
                on_name = False
                for char in str(e):
                    if on_name:
                        name += char
                    if char == "'":
                        on_name = not on_name

                ecrire_console(f"la variable '{name[:-1]}' n'est pas definie, ligne {code.index(line) + 1}")
            except Exception as e:
                ecrire_console(e)

        elif line != "":
            ecrire_console(f"la commande n'existe pas, ligne {code.index(line) + 1}")
        print(var)

window = Tk()

window.title("mini-langage")
window.geometry("800x600")
window.config(background='#314158')
frameT = Frame(window)
frameB = Frame(window)

zone_text = Text(frameR, width=100, height=50)
execute_btn = Button(frameR, command=split_code, text="executer")

console = Text(frameG, width=100, height=13)

frameR.grid(column=0, row=0)
frameG.grid(column=1, row=0)

execute_btn.grid(column=0, row=0)
zone_text.grid(column=0, row=1)


console.pack()
console.config(state=DISABLED)

window.mainloop()