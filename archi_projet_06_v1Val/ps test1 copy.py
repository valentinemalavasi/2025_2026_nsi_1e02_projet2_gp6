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
        
        # Variables pour les filtres
        self.annee_var = tk.StringVar(value="Toutes")
        self.type_crime_var = tk.StringVar(value="Tous")
        self.departement_var = tk.StringVar(value="Tous")
        self.type_graphique_var = tk.StringVar(value="Barres")
        
        self.creer_fenetre()
    
    def creer_fenetre(self):
        # Cadre principal
        cadre_principal = tk.Frame(self.root, bg='white')
        cadre_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Titre
        titre = tk.Label(cadre_principal, text="CRIMES EN FRANCE", 
                        font=("Arial", 24, "bold"), bg='white', fg='black')
        titre.pack(pady=(0, 20))
        
        # Cadre des filtres
        cadre_filtres = tk.LabelFrame(cadre_principal, text="FILTRES", 
                                     font=("Arial", 12, "bold"), bg='white', fg='black',
                                     padx=20, pady=15, relief=tk.GROOVE, bd=2)
        cadre_filtres.pack(fill=tk.X, pady=(0, 20))
        
        # Récupérer les listes
        liste_annees = ["Toutes"] + sorted(self.donnees['annee'].unique().tolist())
        liste_crimes = ["Tous"] + sorted(self.donnees['indicateur'].unique().tolist())
        liste_departements = ["Tous"] + sorted(self.donnees['Code_departement'].unique().tolist())
        
        # Ligne 1: Année et Type de crime
        ligne1 = tk.Frame(cadre_filtres, bg='white')
        ligne1.pack(fill=tk.X, pady=5)
        
        tk.Label(ligne1, text="Année:", font=("Arial", 11), bg='white', fg='black').pack(side=tk.LEFT, padx=(0, 10))
        annee_combo = ttk.Combobox(ligne1, textvariable=self.annee_var, values=liste_annees, 
                                   state='readonly', width=15)
        annee_combo.pack(side=tk.LEFT, padx=(0, 30))
        
        tk.Label(ligne1, text="Type de crime:", font=("Arial", 11), bg='white', fg='black').pack(side=tk.LEFT, padx=(0, 10))
        crime_combo = ttk.Combobox(ligne1, textvariable=self.type_crime_var, values=liste_crimes, 
                                   state='readonly', width=30)
        crime_combo.pack(side=tk.LEFT)
        
        # Ligne 2: Département et Type de graphique
        ligne2 = tk.Frame(cadre_filtres, bg='white')
        ligne2.pack(fill=tk.X, pady=5)
        
        tk.Label(ligne2, text="Département:", font=("Arial", 11), bg='white', fg='black').pack(side=tk.LEFT, padx=(0, 10))
        dept_combo = ttk.Combobox(ligne2, textvariable=self.departement_var, values=liste_departements, 
                                  state='readonly', width=15)
        dept_combo.pack(side=tk.LEFT, padx=(0, 30))
        
        tk.Label(ligne2, text="Type de graphique:", font=("Arial", 11), bg='white', fg='black').pack(side=tk.LEFT, padx=(0, 10))
        graph_combo = ttk.Combobox(ligne2, textvariable=self.type_graphique_var, 
                                   values=["Barres", "Camembert", "Courbes"], 
                                   state='readonly', width=15)
        graph_combo.pack(side=tk.LEFT)
        
        # Bouton de génération
        bouton_generer = tk.Button(cadre_filtres, text="CRÉER LE GRAPHIQUE", 
                                  font=("Arial", 12, "bold"), bg='green', fg='white',
                                  command=self.creer_graphique, padx=20, pady=10,
                                  activebackground='darkgreen', activeforeground='white')
        bouton_generer.pack(pady=(15, 0))
        
        # Cadre pour le graphique
        self.cadre_graphique = tk.Frame(cadre_principal, bg='white')
        self.cadre_graphique.pack(fill=tk.BOTH, expand=True)
    
    def filtrer_donnees(self):
        donnees_filtrees = self.donnees.copy()
        
        # Appliquer les filtres
        if self.annee_var.get() != "Toutes":
            donnees_filtrees = donnees_filtrees[donnees_filtrees['annee'] == int(self.annee_var.get())]
        
        if self.type_crime_var.get() != "Tous":
            donnees_filtrees = donnees_filtrees[donnees_filtrees['indicateur'] == self.type_crime_var.get()]
        
        if self.departement_var.get() != "Tous":
            donnees_filtrees = donnees_filtrees[donnees_filtrees['Code_departement'] == self.departement_var.get()]
        
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
        type_graph = self.type_graphique_var.get()
        
        # Désactiver la notation scientifique
        ax.ticklabel_format(style='plain', axis='y')
        
        # Préparer les données selon les filtres
        if self.annee_var.get() == "Toutes" and self.type_crime_var.get() != "Tous":
            # Évolution d'un type de crime par année
            data = donnees_filtrees.groupby('annee')['nombre'].sum().reset_index()
            self.faire_graphique_evolution(ax, data, type_graph)
            
        elif self.annee_var.get() != "Toutes" and self.type_crime_var.get() == "Tous":
            # Répartition des types de crimes pour une année
            data = donnees_filtrees.groupby('indicateur')['nombre'].sum().reset_index()
            data = data.sort_values('nombre', ascending=False).head(10)
            self.faire_graphique_repartition(ax, data, type_graph)
            
        elif self.departement_var.get() != "Tous":
            # Données pour un département spécifique
            if self.annee_var.get() == "Toutes":
                data = donnees_filtrees.groupby('annee')['nombre'].sum().reset_index()
                self.faire_graphique_evolution(ax, data, type_graph)
            else:
                data = donnees_filtrees.groupby('indicateur')['nombre'].sum().reset_index()
                data = data.sort_values('nombre', ascending=False).head(10)
                self.faire_graphique_repartition(ax, data, type_graph)
        else:
            # Vue globale
            data = donnees_filtrees.groupby('indicateur')['nombre'].sum().reset_index()
            data = data.sort_values('nombre', ascending=False).head(10)
            self.faire_graphique_repartition(ax, data, type_graph)
        
        # Afficher le graphique
        canvas = FigureCanvasTkAgg(fig, master=self.cadre_graphique)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def faire_graphique_evolution(self, ax, data, type_graph):
        annees = data['annee'].astype(int).tolist()
        valeurs = data['nombre'].tolist()
        
        if type_graph == "Courbes":
            ax.plot(annees, valeurs, marker='o', linewidth=2, color='red')
            # Ajouter les valeurs
            for i, (x, y) in enumerate(zip(annees, valeurs)):
                ax.annotate(f'{y:,}', (x, y), textcoords="offset points", 
                           xytext=(0,10), ha='center', fontsize=9)
        else:
            ax.bar(annees, valeurs, color='green', alpha=0.7)
            # Ajouter les valeurs sur les barres
            for i, v in enumerate(valeurs):
                ax.text(annees[i], v + max(valeurs)*0.01, f'{v:,}', 
                       ha='center', fontsize=9)
        
        ax.set_xlabel('Année', fontsize=12)
        ax.set_ylabel('Nombre de crimes', fontsize=12)
        ax.set_title('Évolution des crimes', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(annees, rotation=45)
        plt.tight_layout()
    
    def faire_graphique_repartition(self, ax, data, type_graph):
        labels = data['indicateur'].tolist()
        valeurs = data['nombre'].tolist()
        
        if type_graph == "Camembert":
            ax.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.set_title('Répartition des crimes', fontsize=14, fontweight='bold')
        else:
            # Barres verticales
            ax.bar(range(len(labels)), valeurs, color='green', alpha=0.7)
            ax.set_xticks(range(len(labels)))
            ax.set_xticklabels(labels, rotation=45, ha='right')
            ax.set_ylabel('Nombre de crimes', fontsize=12)
            ax.set_title('Top 10 des crimes', fontsize=14, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            
            # Ajouter les valeurs sur les barres
            for i, v in enumerate(valeurs):
                ax.text(i, v + max(valeurs)*0.01, f'{v:,}', 
                       ha='center', fontsize=9)
        
        plt.tight_layout()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCrimes(root)
    root.mainloop()