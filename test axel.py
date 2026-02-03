from tkinter import * 

# cree une premiere fenètre 

window = Tk()

# personalisation de cette fenètre
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
window.title("stan est tres nul en python")
=======
window.title("app")
>>>>>>> Stashed changes
=======
window.title("app")
>>>>>>> Stashed changes
=======
window.title("app")
>>>>>>> Stashed changes
window.geometry("1080x720")
window.minsize (480, 360)
# crée une boite pour que les elements reste la ou ils doivent etre

frame = Frame(window,bg='#AFAFAF')

# ajouter le texte 

label_title = Label(frame, text="Bienvenue sur cette application", font=("Courrier",40), fg="black")
label_title.pack()

label_subtitle = Label(frame, text="salut", font=("Courrier",25), fg="black")
label_subtitle.pack()

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
# ajouter

frame.pack(expand=YES)
=======
# ajouter un bouton 
>>>>>>> Stashed changes

=======
# ajouter un bouton 

>>>>>>> Stashed changes
=======
# ajouter un bouton 

>>>>>>> Stashed changes
bouton_graph = Button(window , text="Graphique" ,font=("Courrier",40), fg="black" , bg='grey' )
bouton_graph.pack
# afficher

window.mainloop ()