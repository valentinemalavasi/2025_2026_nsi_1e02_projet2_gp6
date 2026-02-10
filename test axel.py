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
fil_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configuartion de la fenetre pour ajouter cette menu bar
window.config (menu=menu_bar)


#demander a chat pour enregistrer les recherches si on veut dans bar menu


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