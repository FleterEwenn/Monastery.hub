#Projet : monastery.hub
#Auteurs : Ewenn Fleter, Raphael Kermes

import tkinter as tk
import random

DUREE = 360           #config
NB_QUESTIONS = 10

#var
score = 0                          
question_actuelle = 0
nombre_a_convertir = 0
temps_restant = DUREE
mode = "binaire"
timer_id = None

#f°

def demarrer_timer():
    global temps_restant, timer_id

    minutes = temps_restant // 60
    secondes = temps_restant % 60
    label_timer.config(text=f"Temps restant : {minutes:02d}:{secondes:02d}")

    #timer rouge à partir de 30 sec
    if temps_restant <= 30:
        label_timer.config(fg="red")
    else:
        label_timer.config(fg="#00FFFF")

    if temps_restant > 0:
        temps_restant -= 1
        timer_id = fenetre.after(1000, demarrer_timer)
    else:
        fin_du_jeu()

def nouvelle_question():
    global nombre_a_convertir

    nombre_a_convertir = random.randint(1, 255)

    if mode == "binaire":
        label_question.config(text=f"Question {question_actuelle+1}/{NB_QUESTIONS}\nConvertir en BINAIRE : {nombre_a_convertir}")
    else:
        label_question.config(text=f"Question {question_actuelle+1}/{NB_QUESTIONS}\nConvertir en HEXADECIMAL : {nombre_a_convertir}")

    entry_reponse.delete(0, tk.END)
    label_resultat.config(text="")
    bouton_verifier.config(state="normal")
    bouton_suivant.config(state="disabled")

def verifier_reponse():
    global score

    reponse = entry_reponse.get().lower()

    if mode == "binaire":
        bonne_reponse = bin(nombre_a_convertir)[2:]
    else:
        bonne_reponse = hex(nombre_a_convertir)[2:]

    if reponse == bonne_reponse:
        score += 1
        label_resultat.config(text=" Correct !", fg="#00FFFF")
    else:
        label_resultat.config(text=f" Faux ! Réponse : {bonne_reponse}", fg="red")

    label_score.config(text=f"Score : {score}/{question_actuelle+1}")

    bouton_verifier.config(state="disabled")
    bouton_suivant.config(state="normal")

def question_suivante():
    global question_actuelle

    question_actuelle += 1

    if question_actuelle >= NB_QUESTIONS:
        fin_du_jeu()
    else:
        nouvelle_question()

def fin_du_jeu():
    global timer_id

    if timer_id:
        fenetre.after_cancel(timer_id)

    label_question.config(text="Quizz terminé !")
    label_resultat.config(text=f"Score final : {score}/{NB_QUESTIONS}", fg="white")
    bouton_verifier.config(state="disabled")
    bouton_suivant.config(state="disabled")

def recommencer():
    global score, question_actuelle, temps_restant, timer_id

    if timer_id:
        fenetre.after_cancel(timer_id)

    score = 0
    question_actuelle = 0
    temps_restant = DUREE

    label_score.config(text="Score : 0/0")
    label_resultat.config(text="")
    label_timer.config(fg="#00FFFF")

    nouvelle_question()
    demarrer_timer()

def choisir_binaire():
    global mode
    mode = "binaire"
    recommencer()

def choisir_hexa():
    global mode
    mode = "hexa"
    recommencer()

def afficher_rappel():
    fenetre_rappel = tk.Toplevel()
    fenetre_rappel.title("Rappel Binaire / Hexa")
    fenetre_rappel.configure(bg="#111111")
    fenetre_rappel.geometry("700x500")  ######## ajustement

    label_titre = tk.Label(
        fenetre_rappel,
        fg="#00FFFF",
        bg="#111111"
    )
    label_titre.pack(pady=10)

    image = tk.PhotoImage(file="rappel.png")

    label_image = tk.Label(
        fenetre_rappel,
        image=image,
        bg="#111111"
    )
    label_image.image = image  #pr pas dispawn
    label_image.pack(pady=10)

#les fenetres

fenetre = tk.Tk()
fenetre.title("NSI LEGO Quizz")
fenetre.geometry("500x600")
fenetre.configure(bg="#111111")
fenetre.resizable(False, False)

label_titre = tk.Label(
    fenetre,
    text="QUIZZ CONVERSION",
    font=("Arial", 18, "bold"),
    fg="#00FFFF",
    bg="#111111"
)
label_titre.pack(pady=15)

label_timer = tk.Label(
    fenetre,
    text="Temps restant : 06:00",
    font=("Arial", 14),
    fg="#00FFFF",
    bg="#111111"
)
label_timer.pack()

label_question = tk.Label(
    fenetre,
    text="",
    font=("Arial", 14),
    fg="white",
    bg="#111111"
)
label_question.pack(pady=20)

entry_reponse = tk.Entry(
    fenetre,
    font=("Arial", 14),
    bg="#222222",
    fg="#00FFFF",
    insertbackground="white",
    justify="center"
)
entry_reponse.pack(pady=10)

bouton_verifier = tk.Button(
    fenetre,
    text="Vérifier",
    command=verifier_reponse,
    bg="#00FFFF",
    fg="black",
    font=("Arial", 12, "bold")
)
bouton_verifier.pack(pady=10)

bouton_suivant = tk.Button(
    fenetre,
    text="Question suivante",
    command=question_suivante,
    bg="#444444",
    fg="#00FFFF",
    state="disabled"
)
bouton_suivant.pack(pady=5)

label_resultat = tk.Label(
    fenetre,
    text="",
    font=("Arial", 12),
    bg="#111111"
)
label_resultat.pack(pady=5)

label_score = tk.Label(
    fenetre,
    text="Score : 0/0",
    font=("Arial", 12),
    fg="white",
    bg="#111111"
)
label_score.pack(pady=10)

frame_modes = tk.Frame(fenetre, bg="#111111")
frame_modes.pack(pady=10)

tk.Button(frame_modes, text="Mode Binaire",
          command=choisir_binaire,
          bg="#00FFFF", fg="black").pack(side="left", padx=10)

tk.Button(frame_modes, text="Mode Hexa",
          command=choisir_hexa,
          bg="#00FFFF", fg="black").pack(side="left", padx=10)

tk.Button(fenetre, text="Recommencer",
          command=recommencer,
          bg="#333333", fg="#00FFFF").pack(pady=15)

tk.Button(
    fenetre,
    text="Besoin d'un rappel ?",
    command=afficher_rappel,
    bg="#222222",
    fg="#00FFFF"
).pack(pady=10)

#lancement
nouvelle_question()
demarrer_timer()

fenetre.mainloop()
