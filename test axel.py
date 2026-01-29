from tkinter import * 

# cree une premiere fenètre 

window = Tk()

# personalisation de cette fenètre
window.title("stan est tres nul en python")
window.geometry("1080x720")
window.minsize (480, 360)
# crée une boite pour que les elements reste la ou ils doivent etre

frame = Frame(window,bg='#AFAFAF')

# ajouter le texte 

label_title = Label(frame, text="Bienvenue sur cette application", font=("Courrier",40), fg="black")
label_title.pack()

label_subtitle = Label(frame, text="salut", font=("Courrier",25), fg="black")
label_subtitle.pack()

# ajouter

frame.pack(expand=YES)

# afficher

window.mainloop ()