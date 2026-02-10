from tkinter import * 

# cree une premiere fenètre 

window = Tk()

# personalisation de cette fenètre


window.title("app")

window.geometry("1080x720")
window.minsize (480, 360)
window.config (bg='white')

# crée une boite pour que les elements reste la ou ils doivent etre

frame = Frame(window,bg='#AFAFAF',bd=1, relief= SUNKEN)

# ajouter le texte 

label_title = Label(window, text="Bienvenue! selectionner vos paramètres ", font=("Courrier",40), fg="black", bg='white')
label_title.pack()

#création d'une barre menu
menu_bar = Menu(window) 
#creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau")
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configuartion de la fenetre pour ajouter cette menu bar
window.config (menu=menu_bar)


#faire un bouton save pour la recherche
def save_recherche():
    with open("recherches.txt", "a", encoding="utf-8") as f:
        f.write("f"Année: {annee_crime}, Type: {type_crime}, Département: {departement}\n")
btn_save = Button(
    frame,
    text="Save",
    font=("Arial", 11),
    command=save_recherche
)
btn_save.pack(pady=30)

# ajouter

frame.pack(expand=YES)


# ajouter un bouton 

bouton_valider = Button(frame, text="Années du crime", font=("Arial", 11))
bouton_valider.pack(pady=50)

bouton_valider = Button(frame, text="Type de crime", font=("Arial", 11))
bouton_valider.pack(pady=50)

bouton_valider = Button(frame, text="Département du crime", font=("Arial", 11))
bouton_valider.pack(pady=50)


# afficher

window.mainloop ()