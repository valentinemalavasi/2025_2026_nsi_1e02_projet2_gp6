from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import model
import view_graph

class Controller:
    def __init__(self, root, view):
        self.root = root
        self.view = view

        self.donnees = model.charger_donnees()
        if self.donnees is None:
            messagebox.showerror("Erreur", "Impossible de charger le fichier CSV.")
            root.destroy()
            return

    def creer_graphique(self, annee, crime, dept, type_graph, cadre_graphique):
        for widget in cadre_graphique.winfo_children():
            widget.destroy()

        df = model.filtrer_donnees(self.donnees, annee, crime, dept)

        if df.empty:
            messagebox.showwarning("Attention", "Aucune donnée trouvée.")
            return

        fig, ax = plt.subplots(figsize=(10, 6))

        if annee == "Toutes" and crime != "Tous":
            data = model.data_evolution(df)

            if type_graph == "Courbes" and len(data) < 2:
                messagebox.showerror("Erreur", "Impossible de créer une courbe : au moins 2 années nécessaires.")
                return

            view_graph.graphique_evolution(ax, data, type_graph)

        else:
            data = model.data_repartition(df)

            if type_graph == "Camembert" and len(data) < 2:
                messagebox.showerror("Erreur", "Impossible de créer un camembert : au moins 2 catégories nécessaires.")
                return

            view_graph.graphique_repartition(ax, data, type_graph)

        canvas = FigureCanvasTkAgg(fig, master=cadre_graphique)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)