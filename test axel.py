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

label_title = Label(window, text="Bienvenue ", font=("Courrier",40), fg="black", bg='white')
label_title.pack()

label_subtitle = Label(frame , text="année ", font=("Courrier",25), fg="black", bg='white')
label_subtitle.pack()


# ajouter

frame.pack(expand=YES)


# ajouter un bouton 

bouton_graph = Button(window , text="Graphique" ,font=("Courrier",40), fg="black" , bg='grey' )
bouton_graph.pack
# afficher

window.mainloop ()