#Projet : monastery.hub
#Auteurs : Ewenn Fleter, Raphael Kermes

from tkinter import *
from string import *
from random import *

window = Tk()

window.title("Check Password")
window.geometry("800x600")

def evaluate_password(password:str):
    # peut être conseiller à voir ce site ?
    # https://www.cybermalveillance.gouv.fr/tous-nos-contenus/bonnes-pratiques/mots-de-passe#:~:text=Utilisez%20un%20mot%20de%20passe%20suffisamment%20long%20et%20complexe&text=Pour%20emp%C3%AAcher%20ce%20type%20d,chiffres%20et%20des%20caract%C3%A8res%20sp%C3%A9ciaux.

    point = 20
    dontuse_list = ['abcde', '1234', '0000', 'azerty', 'motdepasse', 'mdp'] # liste non exhaustive
    char_spe = punctuation
    nb_char_spe = 0
    chiffre = digits
    nb_chiffre = 0
    lettre = ascii_letters
    nb_lettre = 0

    # verification de mot de passe à fortifiée
    for pattern in dontuse_list :
        if pattern in password:
            point -= 20
    
    for char in password:
        if char in char_spe:
            nb_char_spe += 1
        elif char in chiffre:
            nb_chiffre += 1
        elif char in lettre:
            nb_lettre += 1

    if nb_char_spe < 3:
        point -= 3
    if nb_chiffre < 3:
        point -= 3
    if nb_lettre < 3:
        point -= 3
    
    if nb_char_spe >= 4 and nb_chiffre >= 4 and nb_lettre >= 4:
        point += 5

    if len(password) < 7:
        point -= 10
    elif len(password) < 10:
        point -= 5
    elif len(password) < 12:
        point -= 1
    
    if point <= 0:
        response = "Votre mot de passe est completement nul"
        label_color = 'red'
    elif point <= 10:
        response = "Votre mot de passe est très faible, vous devez impérativement le changer et l'améliorer"
        label_color = 'red'
    elif point <= 15:
        response = "Votre mot de passe est faible, améliorez le vite"
        label_color = 'orange'
    elif point < 20:
        response = "Votre mot de passe est moyen, l'utiliser trop lontemps pourrait devenir critique"
        label_color = 'lightgreen'
    elif point >= 20:
        response = "Bravo, votre mot de passe est fort"
        label_color = 'green'

    label_check = Label(window, text=response, fg=label_color)
    
    label_check.pack()
    label_check.after(3000, label_check.destroy)

def check_password(frame:Frame):
    frame.destroy()

    checkpwd_frame = Frame(window)
    checkpwd_frame.pack(pady=50)

    password_entry = Entry(checkpwd_frame)
    valid_btn = Button(checkpwd_frame, text="Valider", command=lambda:evaluate_password(str(password_entry.get())))

    password_entry.pack()
    valid_btn.pack()

def generate_pwd(frame:Frame, length:int):
    charspe = punctuation
    chiffre = digits
    letter = ascii_letters

    nb_charspe = length//3 + length%3
    nb_chiffre = length//3
    nb_letter = length//3

    password = []

    while len(password) < length:
        if nb_charspe > 0:
            password.append(charspe[randint(0, len(charspe)-1)])
            nb_charspe -= 1
        if nb_chiffre > 0:
            password.append(chiffre[randint(0, len(chiffre)-1)])
            nb_chiffre -= 1
        if nb_letter > 0:
            password.append(letter[randint(0, len(letter)-1)])
            nb_letter -= 1
    
    shuffle(password)
    password = ''.join(password)

    label_pwd = Label(frame, text=f"Votre mot de passe est : {password}")
    label_pwd.pack()
    label_pwd.after(5000, label_pwd.destroy)

def generate_pwd_menu(frame:Frame):
    frame.destroy()

    genpwd_frame = Frame(window)
    genpwd_frame.pack(pady=50)

    label_lenght = Label(genpwd_frame, text="Choisissez la longueur du mot de passe souhaité")
    label_lenght.pack()

    lenght_scale = Scale(genpwd_frame, from_=10, to=50, orient=HORIZONTAL)
    lenght_scale.pack()

    btn_genpwd = Button(genpwd_frame, text="générer mot de passe", command=lambda:generate_pwd(genpwd_frame, lenght_scale.get()))
    btn_genpwd.pack()

def main():
    main_frame = Frame(window)
    main_frame.pack(pady=50)

    btn_check = Button(main_frame, text="Verifier mot de passe", command=lambda:check_password(main_frame))
    btn_generate = Button(main_frame, text="Générer mot de passe sécurisé", command=lambda:generate_pwd_menu(main_frame))

    btn_check.pack()
    btn_generate.pack()

main()

window.mainloop()