import tkinter as tk
from tkinter import StringVar

import model
import view_main_window
from controler_view_main_window import Controller

root = tk.Tk()

# Variables
annee_var = StringVar(value="Toutes")
crime_var = StringVar(value="Tous")
dept_var = StringVar(value="Tous")
type_graph_var = StringVar(value="Barres")

donnees = model.charger_donnees()
liste_annees = ["Toutes"] + sorted(donnees["annee"].unique().tolist())
liste_crimes = ["Tous"] + sorted(donnees["indicateur"].unique().tolist())
liste_departements = ["Tous"] + sorted(donnees["Code_departement"].unique().tolist())

controller = Controller(root, view_main_window)

cadre_graphique = view_main_window.creer_fenetre(
    root,
    liste_annees,
    liste_crimes,
    liste_departements,
    type_graph_var,
    annee_var,
    crime_var,
    dept_var,
    lambda: controller.creer_graphique(
        annee_var.get(),
        crime_var.get(),
        dept_var.get(),
        type_graph_var.get(),
        cadre_graphique
    )
)

root.mainloop()