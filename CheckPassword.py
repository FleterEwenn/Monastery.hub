from tkinter import *

window = Tk()

window.title("Check Password")
window.geometry("800x600")

def evaluate_password(password:str):
    # peut être conseiller à voir ce site ?
    #  https://www.cybermalveillance.gouv.fr/tous-nos-contenus/bonnes-pratiques/mots-de-passe#:~:text=Utilisez%20un%20mot%20de%20passe%20suffisamment%20long%20et%20complexe&text=Pour%20emp%C3%AAcher%20ce%20type%20d,chiffres%20et%20des%20caract%C3%A8res%20sp%C3%A9ciaux.

    point = 20
    dontuse_list = ['abcde', '1234', '0000', 'azerty', 'motdepasse'] # liste non exhaustive

    # verification de mot de passe à fortifiée
    for pattern in dontuse_list :
        if pattern in password:
            point -= 10

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
        response = "Votre mot de passe et moyen, l'utiliser trop longtemps pourrait deveni critique"
        label_color = 'lightgreen'
    elif point == 20:
        response = "Bravo, votre mot de passe est fort, nous vous conseillons de changer régulièrement de mot de passe pour garantir une certaine sécurité"
        label_color = 'green'

    label_check = Label(window, text=response, fg=label_color)
    
    label_check.pack()

def check_password(frame:Frame):
    frame.destroy()

    checkpwd_frame = Frame(window)
    checkpwd_frame.pack(pady=50)

    password_entry = Entry(checkpwd_frame)
    valid_btn = Button(checkpwd_frame, text="Valider", command=lambda:evaluate_password(str(password_entry.get())))

    password_entry.pack()
    valid_btn.pack()

def main():
    main_frame = Frame(window)
    main_frame.pack(pady=50)

    btn_check = Button(main_frame, text="Verifier mot de passe", command=lambda:check_password(main_frame))
    btn_generate = Button(main_frame, text="Générer mot de passe sécurisé")

    btn_check.pack()
    btn_generate.pack()

main()

window.mainloop()