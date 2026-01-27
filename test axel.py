from tkinter import * 

# cree une premiere fenètre 

window = Tk()

# personalisation de cette fenètre
window.title("stan est tres fort en python")
window.geometry("1080x720")
window.minsize (480, 360)

# ajouter le texte 

label_title = Label(window, text="Bienvenue sur cette application", font=("Courrier",40), fg="black")
label_title.pack(expand=YES)

label_subtitle = Label(window, text="salut", font=("Courrier",40), fg="black")
label_subtitle.pack(expand=YES)


# afficher

window.mainloop ()