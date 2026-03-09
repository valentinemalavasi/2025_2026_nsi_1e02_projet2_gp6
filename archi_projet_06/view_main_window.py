import tkinter as tk
from tkinter import ttk

def creer_fenetre(root, liste_annees, liste_crimes, liste_departements, type_graph_var,
                  annee_var, crime_var, dept_var, callback_creer_graphique):

    root.title("Crimes en France")
    root.geometry("1200x800")
    root.config(bg="white")

    cadre_principal = tk.Frame(root, bg="white")
    cadre_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    titre = tk.Label(cadre_principal, text="CRIMES EN FRANCE",
                     font=("Arial", 24, "bold"), bg="white")
    titre.pack(pady=(0, 20))

    cadre_filtres = tk.LabelFrame(cadre_principal, text="FILTRES",
                                  font=("Arial", 12, "bold"), bg="white",
                                  padx=20, pady=15)
    cadre_filtres.pack(fill=tk.X, pady=(0, 20))

    # Ligne 1
    ligne1 = tk.Frame(cadre_filtres, bg="white")
    ligne1.pack(fill=tk.X, pady=5)

    tk.Label(ligne1, text="Année :", bg="white").pack(side=tk.LEFT)
    ttk.Combobox(ligne1, textvariable=annee_var, values=liste_annees,
                 state="readonly", width=15).pack(side=tk.LEFT, padx=20)

    tk.Label(ligne1, text="Type de crime :", bg="white").pack(side=tk.LEFT)
    ttk.Combobox(ligne1, textvariable=crime_var, values=liste_crimes,
                 state="readonly", width=30).pack(side=tk.LEFT)

    # Ligne 2
    ligne2 = tk.Frame(cadre_filtres, bg="white")
    ligne2.pack(fill=tk.X, pady=5)

    tk.Label(ligne2, text="Département :", bg="white").pack(side=tk.LEFT)
    ttk.Combobox(ligne2, textvariable=dept_var, values=liste_departements,
                 state="readonly", width=15).pack(side=tk.LEFT, padx=20)

    tk.Label(ligne2, text="Type de graphique :", bg="white").pack(side=tk.LEFT)
    ttk.Combobox(ligne2, textvariable=type_graph_var,
                 values=["Barres", "Camembert", "Courbes"],
                 state="readonly", width=15).pack(side=tk.LEFT)

    # Bouton
    tk.Button(cadre_filtres, text="CRÉER LE GRAPHIQUE",
              font=("Arial", 12, "bold"), bg="green", fg="white",
              command=callback_creer_graphique).pack(pady=10)

    # Cadre graphique
    cadre_graphique = tk.Frame(cadre_principal, bg="white")
    cadre_graphique.pack(fill=tk.BOTH, expand=True)

    return cadre_graphique