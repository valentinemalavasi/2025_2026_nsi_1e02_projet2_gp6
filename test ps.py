import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AppCrimes:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyse des Crimes en France")
        self.root.geometry("1200x800")
        self.root.config(bg='white')
        
        # Charger les données
        try:
            self.df = pd.read_csv("InfoCrimes.csv", sep=";")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger le fichier CSV: {e}")
            return
        
        # Variables pour les filtres
        self.annee_var = tk.StringVar(value="Toutes")
        self.type_crime_var = tk.StringVar(value="Tous")
        self.departement_var = tk.StringVar(value="Tous")
        self.type_graphique_var = tk.StringVar(value="Barres")
        
        self.creer_interface()
    
    def creer_interface(self):
        # Frame principale
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Titre
        titre = tk.Label(main_frame, text="Analyse des Crimes en France", 
                        font=("Arial", 24, "bold"), bg='white', fg='#2c3e50')
        titre.pack(pady=(0, 20))
        
        # Frame des filtres
        filtres_frame = tk.LabelFrame(main_frame, text="Filtres de recherche", 
                                     font=("Arial", 12, "bold"), bg='#ecf0f1', 
                                     padx=20, pady=15)
        filtres_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Récupérer les valeurs uniques
        annees = ["Toutes"] + sorted(self.df['annee'].unique().tolist())
        types_crimes = ["Tous"] + sorted(self.df['indicateur'].unique().tolist())
        departements = ["Tous"] + sorted(self.df['Code_departement'].unique().tolist())
        
        # Ligne 1: Année et Type de crime
        row1 = tk.Frame(filtres_frame, bg='#ecf0f1')
        row1.pack(fill=tk.X, pady=5)
        
        tk.Label(row1, text="Année:", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=(0, 10))
        annee_combo = ttk.Combobox(row1, textvariable=self.annee_var, values=annees, 
                                   state='readonly', width=15)
        annee_combo.pack(side=tk.LEFT, padx=(0, 30))
        
        tk.Label(row1, text="Type de crime:", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=(0, 10))
        crime_combo = ttk.Combobox(row1, textvariable=self.type_crime_var, values=types_crimes, 
                                   state='readonly', width=30)
        crime_combo.pack(side=tk.LEFT)
        
        # Ligne 2: Département et Type de graphique
        row2 = tk.Frame(filtres_frame, bg='#ecf0f1')
        row2.pack(fill=tk.X, pady=5)
        
        tk.Label(row2, text="Département:", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=(0, 10))
        dept_combo = ttk.Combobox(row2, textvariable=self.departement_var, values=departements, 
                                  state='readonly', width=15)
        dept_combo.pack(side=tk.LEFT, padx=(0, 30))
        
        tk.Label(row2, text="Type de graphique:", font=("Arial", 11), bg='#ecf0f1').pack(side=tk.LEFT, padx=(0, 10))
        graph_combo = ttk.Combobox(row2, textvariable=self.type_graphique_var, 
                                   values=["Barres", "Camembert", "Courbes", "Barres empilées"], 
                                   state='readonly', width=20)
        graph_combo.pack(side=tk.LEFT)
        
        # Bouton de génération
        btn_generer = tk.Button(filtres_frame, text="Générer le graphique", 
                               font=("Arial", 12, "bold"), bg='#3498db', fg='white',
                               command=self.generer_graphique, cursor='hand2',
                               padx=20, pady=10)
        btn_generer.pack(pady=(15, 0))
        
        # Frame pour le graphique
        self.graph_frame = tk.Frame(main_frame, bg='white')
        self.graph_frame.pack(fill=tk.BOTH, expand=True)
    
    def filtrer_donnees(self):
        df_filtre = self.df.copy()
        
        # Appliquer les filtres
        if self.annee_var.get() != "Toutes":
            df_filtre = df_filtre[df_filtre['annee'] == int(self.annee_var.get())]
        
        if self.type_crime_var.get() != "Tous":
            df_filtre = df_filtre[df_filtre['indicateur'] == self.type_crime_var.get()]
        
        if self.departement_var.get() != "Tous":
            df_filtre = df_filtre[df_filtre['Code_departement'] == self.departement_var.get()]
        
        return df_filtre

    
    def generer_graphique(self):
        # Nettoyer le frame précédent
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Filtrer les données
        df_filtre = self.filtrer_donnees()
        
        if df_filtre.empty:
            messagebox.showwarning("Aucune donnée", "Aucune donnée ne correspond aux filtres sélectionnés.")
            return
        
        # Créer la figure
        fig, ax = plt.subplots(figsize=(10, 6))
        type_graph = self.type_graphique_var.get()
        
        # Préparer les données selon les filtres
        if self.annee_var.get() == "Toutes" and self.type_crime_var.get() != "Tous":
            # Évolution d'un type de crime par année
            data = df_filtre.groupby('annee')['nombre'].sum().reset_index()
            self.creer_graphique_evolution(ax, data, type_graph)
            
        elif self.annee_var.get() != "Toutes" and self.type_crime_var.get() == "Tous":
            # Répartition des types de crimes pour une année
            data = df_filtre.groupby('indicateur')['nombre'].sum().reset_index()
            data = data.sort_values('nombre', ascending=False).head(10)
            self.creer_graphique_repartition(ax, data, type_graph)
            
        elif self.departement_var.get() != "Tous":
            # Données pour un département spécifique
            if self.annee_var.get() == "Toutes":
                data = df_filtre.groupby('annee')['nombre'].sum().reset_index()
                self.creer_graphique_evolution(ax, data, type_graph)
            else:
                data = df_filtre.groupby('indicateur')['nombre'].sum().reset_index()
                data = data.sort_values('nombre', ascending=False).head(10)
                self.creer_graphique_repartition(ax, data, type_graph)
        else:
            # Vue globale
            data = df_filtre.groupby('indicateur')['nombre'].sum().reset_index()
            data = data.sort_values('nombre', ascending=False).head(10)
            self.creer_graphique_repartition(ax, data, type_graph)
        
        # Afficher le graphique dans Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def creer_graphique_evolution(self, ax, data, type_graph):
        if type_graph == "Courbes":
            ax.plot(data['annee'], data['nombre'], marker='o', linewidth=2, color='#e74c3c')
            ax.fill_between(data['annee'], data['nombre'], alpha=0.3, color='#e74c3c')
        else:  # Barres par défaut
            ax.bar(data['annee'], data['nombre'], color='#3498db', alpha=0.7)
        
        ax.set_xlabel('Année', fontsize=12, fontweight='bold')
        ax.set_ylabel('Nombre de crimes', fontsize=12, fontweight='bold')
        ax.set_title(f'Évolution - {self.type_crime_var.get()}', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
    
    def creer_graphique_repartition(self, ax, data, type_graph):
        if type_graph == "Camembert":
            colors = plt.cm.Set3(range(len(data)))
            ax.pie(data['nombre'], labels=data['indicateur'], autopct='%1.1f%%', 
                  colors=colors, startangle=90)
            ax.set_title(f'Répartition des crimes - {self.annee_var.get()}', 
                        fontsize=14, fontweight='bold')
        elif type_graph == "Barres empilées":
            ax.barh(data['indicateur'], data['nombre'], color='#2ecc71', alpha=0.7)
            ax.set_xlabel('Nombre de crimes', fontsize=12, fontweight='bold')
            ax.set_title(f'Top 10 des crimes - {self.annee_var.get()}', 
                        fontsize=14, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)
        else:  # Barres verticales
            ax.bar(range(len(data)), data['nombre'], color='#9b59b6', alpha=0.7)
            ax.set_xticks(range(len(data)))
            ax.set_xticklabels(data['indicateur'], rotation=45, ha='right')
            ax.set_ylabel('Nombre de crimes', fontsize=12, fontweight='bold')
            ax.set_title(f'Top 10 des crimes - {self.annee_var.get()}', 
                        fontsize=14, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCrimes(root)
    root.mainloop()
