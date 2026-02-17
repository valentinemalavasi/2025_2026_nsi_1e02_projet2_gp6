import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AppCrimes:
    def __init__(self, root):
        self.root = root
        self.root.title("Crimes en France")
        self.root.geometry("1200x800")
        self.root.config(bg='white')
        
        # Charger le fichier CSV
        try:
            self.donnees = pd.read_csv("InfoCrimes.csv", sep=";")
        except:
            messagebox.showerror("Erreur", "Impossible de charger le fichier CSV")
            return
        
        # Variable pour le type de graphique
        self.type_graphique = tk.StringVar(value="Barres")
        
        self.creer_fenetre()
    
    def creer_fenetre(self):
        # Cadre principal
        cadre_principal = tk.Frame(self.root, bg='white')
        cadre_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Titre
        titre = tk.Label(cadre_principal, text="Crimes en France", 
                        font=("Arial", 24, "bold"), bg='white')
        titre.pack(pady=(0, 20))
        
        # Cadre des filtres
        cadre_filtres = tk.LabelFrame(cadre_principal, text="Choisir les filtres", 
                                     font=("Arial", 12, "bold"), bg='lightgray', 
                                     padx=20, pady=15)
        cadre_filtres.pack(fill=tk.X, pady=(0, 20))
        
        # Récupérer les listes
        liste_annees = sorted(self.donnees['annee'].unique().tolist())
        liste_crimes = sorted(self.donnees['indicateur'].unique().tolist())
        liste_departements = sorted(self.donnees['Code_departement'].unique().tolist())
        
        # Filtre Années (sélection multiple)
        ligne1 = tk.Frame(cadre_filtres, bg='lightgray')
        ligne1.pack(fill=tk.X, pady=5)
        
        tk.Label(ligne1, text="Années:", font=("Arial", 11), bg='lightgray').pack(side=tk.LEFT, padx=(0, 10))
        cadre_annees = tk.Frame(ligne1, bg='white', relief=tk.SUNKEN, bd=1)
        cadre_annees.pack(side=tk.LEFT, padx=(0, 30))
        
        scroll_annees = tk.Scrollbar(cadre_annees)
        scroll_annees.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.liste_annees = tk.Listbox(cadre_annees, selectmode=tk.MULTIPLE, 
                                       height=4, width=15, yscrollcommand=scroll_annees.set)
        self.liste_annees.pack(side=tk.LEFT)
        scroll_annees.config(command=self.liste_annees.yview)
        
        for annee in liste_annees:
            self.liste_annees.insert(tk.END, annee)
        
        # Filtre Types de crimes (sélection multiple)
        tk.Label(ligne1, text="Types de crimes:", font=("Arial", 11), bg='lightgray').pack(side=tk.LEFT, padx=(0, 10))
        cadre_crimes = tk.Frame(ligne1, bg='white', relief=tk.SUNKEN, bd=1)
        cadre_crimes.pack(side=tk.LEFT)
        
        scroll_crimes = tk.Scrollbar(cadre_crimes)
        scroll_crimes.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.liste_crimes = tk.Listbox(cadre_crimes, selectmode=tk.MULTIPLE, 
                                       height=4, width=30, yscrollcommand=scroll_crimes.set)
        self.liste_crimes.pack(side=tk.LEFT)
        scroll_crimes.config(command=self.liste_crimes.yview)
        
        for crime in liste_crimes:
            self.liste_crimes.insert(tk.END, crime)
        
        # Filtre Départements (sélection multiple)
        ligne2 = tk.Frame(cadre_filtres, bg='lightgray')
        ligne2.pack(fill=tk.X, pady=5)
        
        tk.Label(ligne2, text="Départements:", font=("Arial", 11), bg='lightgray').pack(side=tk.LEFT, padx=(0, 10))
        cadre_depts = tk.Frame(ligne2, bg='white', relief=tk.SUNKEN, bd=1)
        cadre_depts.pack(side=tk.LEFT, padx=(0, 30))
        
        scroll_depts = tk.Scrollbar(cadre_depts)
        scroll_depts.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.liste_depts = tk.Listbox(cadre_depts, selectmode=tk.MULTIPLE, 
                                      height=4, width=15, yscrollcommand=scroll_depts.set)
        self.liste_depts.pack(side=tk.LEFT)
        scroll_depts.config(command=self.liste_depts.yview)
        
        for dept in liste_departements:
            self.liste_depts.insert(tk.END, dept)
        
        # Type de graphique
        tk.Label(ligne2, text="Type de graphique:", font=("Arial", 11), bg='lightgray').pack(side=tk.LEFT, padx=(0, 10))
        choix_graph = ttk.Combobox(ligne2, textvariable=self.type_graphique, 
                                   values=["Barres", "Camembert", "Courbes"], 
                                   state='readonly', width=15)
        choix_graph.pack(side=tk.LEFT)
        
        # Boutons
        ligne_boutons = tk.Frame(cadre_filtres, bg='lightgray')
        ligne_boutons.pack(pady=(15, 0))
        
        bouton_tout = tk.Button(ligne_boutons, text="Tout sélectionner", 
                               font=("Arial", 10), bg='orange', fg='white',
                               command=self.tout_selectionner, padx=10, pady=5)
        bouton_tout.pack(side=tk.LEFT, padx=5)
        
        bouton_rien = tk.Button(ligne_boutons, text="Tout désélectionner", 
                               font=("Arial", 10), bg='red', fg='white',
                               command=self.tout_deselectionner, padx=10, pady=5)
        bouton_rien.pack(side=tk.LEFT, padx=5)
        
        bouton_generer = tk.Button(ligne_boutons, text="Créer le graphique", 
                                  font=("Arial", 12, "bold"), bg='green', fg='white',
                                  command=self.creer_graphique, padx=20, pady=8)
        bouton_generer.pack(side=tk.LEFT, padx=5)
        
        # Cadre pour le graphique
        self.cadre_graphique = tk.Frame(cadre_principal, bg='white')
        self.cadre_graphique.pack(fill=tk.BOTH, expand=True)
    
    def tout_selectionner(self):
        self.liste_annees.select_set(0, tk.END)
        self.liste_crimes.select_set(0, tk.END)
        self.liste_depts.select_set(0, tk.END)
    
    def tout_deselectionner(self):
        self.liste_annees.selection_clear(0, tk.END)
        self.liste_crimes.selection_clear(0, tk.END)
        self.liste_depts.selection_clear(0, tk.END)
    
    def filtrer_donnees(self):
        donnees_filtrees = self.donnees.copy()
        
        # Récupérer les sélections
        annees_selectionnees = [self.liste_annees.get(i) for i in self.liste_annees.curselection()]
        crimes_selectionnes = [self.liste_crimes.get(i) for i in self.liste_crimes.curselection()]
        depts_selectionnes = [self.liste_depts.get(i) for i in self.liste_depts.curselection()]
        
        # Appliquer les filtres
        if annees_selectionnees:
            donnees_filtrees = donnees_filtrees[donnees_filtrees['annee'].isin(annees_selectionnees)]
        
        if crimes_selectionnes:
            donnees_filtrees = donnees_filtrees[donnees_filtrees['indicateur'].isin(crimes_selectionnes)]
        
        if depts_selectionnes:
            donnees_filtrees = donnees_filtrees[donnees_filtrees['Code_departement'].isin(depts_selectionnes)]
        
        return donnees_filtrees
    
    def creer_graphique(self):
        # Nettoyer l'ancien graphique
        for widget in self.cadre_graphique.winfo_children():
            widget.destroy()
        
        # Filtrer les données
        donnees_filtrees = self.filtrer_donnees()
        
        if donnees_filtrees.empty:
            messagebox.showwarning("Attention", "Aucune donnée trouvée avec ces filtres")
            return
        
        # Créer le graphique
        fig, ax = plt.subplots(figsize=(10, 6))
        type_graph = self.type_graphique.get()
        
        # Préparer les données pour le graphique
        annees_selectionnees = [self.liste_annees.get(i) for i in self.liste_annees.curselection()]
        crimes_selectionnes = [self.liste_crimes.get(i) for i in self.liste_crimes.curselection()]
        
        # Si plusieurs années sélectionnées -> graphique d'évolution
        if len(annees_selectionnees) > 1:
            data = donnees_filtrees.groupby('annee')['nombre'].sum().reset_index()
            self.faire_graphique_evolution(ax, data, type_graph)
        else:
            # Sinon -> graphique de répartition
            data = donnees_filtrees.groupby('indicateur')['nombre'].sum().reset_index()
            data = data.sort_values('nombre', ascending=False).head(10)
            self.faire_graphique_repartition(ax, data, type_graph)
        
        # Afficher le graphique
        canvas = FigureCanvasTkAgg(fig, master=self.cadre_graphique)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def faire_graphique_evolution(self, ax, data, type_graph):
        if type_graph == "Courbes":
            ax.plot(data['annee'], data['nombre'], marker='o', linewidth=2, color='red')
            ax.fill_between(data['annee'], data['nombre'], alpha=0.3, color='red')
        else:
            ax.bar(data['annee'], data['nombre'], color='blue', alpha=0.7)
        
        ax.set_xlabel('Année', fontsize=12)
        ax.set_ylabel('Nombre de crimes', fontsize=12)
        ax.set_title('Évolution des crimes', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
    
    def faire_graphique_repartition(self, ax, data, type_graph):
        if type_graph == "Camembert":
            ax.pie(data['nombre'], labels=data['indicateur'], autopct='%1.1f%%', startangle=90)
            ax.set_title('Répartition des crimes', fontsize=14, fontweight='bold')
        else:
            ax.bar(range(len(data)), data['nombre'], color='purple', alpha=0.7)
            ax.set_xticks(range(len(data)))
            ax.set_xticklabels(data['indicateur'], rotation=45, ha='right')
            ax.set_ylabel('Nombre de crimes', fontsize=12)
            ax.set_title('Top 10 des crimes', fontsize=14, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCrimes(root)
    root.mainloop()
