import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lecture du CSV
df = pd.read_csv("InfoCrimes.csv", sep=";")

# Conversion des colonnes numériques
df["annee"] = pd.to_numeric(df["annee"], errors="coerce")
df["nombre"] = pd.to_numeric(df["nombre"], errors="coerce")

# ===== Choix du type de crime =====
type_crime = input("Entrez le type de crime à analyser (ex : Homicides) : ")

# Filtrage sur le type de crime
df_crime = df[df["indicateur"] == type_crime]

# Vérification
if df_crime.empty:
    print(f"Aucune donnée disponible pour le type de crime : {type_crime}")
else:
    # Agrégation : somme des crimes par année
    df_evolution = (
        df_crime.groupby("annee")["nombre"]
        .sum()
        .reset_index()
        .sort_values("annee")
    )

    # Graphique en courbe
    plt.figure(figsize=(10, 5))
    plt.plot(df_evolution["annee"], df_evolution["nombre"], marker="o")

    plt.xlabel("Année")
    plt.ylabel("Nombre de crimes")
    plt.title(f"Évolution du nombre de crimes : {type_crime}")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

