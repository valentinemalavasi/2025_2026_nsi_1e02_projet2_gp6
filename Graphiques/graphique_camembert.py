import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"graphique type de crime par année (camembert), ou l'utilisateur choisit l'année"

# Lecture du CSV
df = pd.read_csv("InfoCrimes.csv", sep=";")

# Conversion des colonnes numériques
df["annee"] = pd.to_numeric(df["annee"], errors="coerce")
df["nombre"] = pd.to_numeric(df["nombre"], errors="coerce")

#  Année choisie par l'utilisateur 
annee_choisie =  2016 #int(input("Entrez l'année à consulter entre 2016 et 2024 : "))

# Filtrage sur l'année
df_annee = df[df["annee"] == annee_choisie]

# Vérification si l'année existe
if df_annee.empty:
    print(f"Aucune donnée disponible pour l'année {annee_choisie}.")
else:
    # Agrégation : somme des crimes par type
    df_grouped = (
        df_annee.groupby("indicateur")["nombre"]
        .sum()
        .reset_index()
    )

    # Graphique en camembert
    plt.figure(figsize=(8, 8))
    plt.pie(
        df_grouped["nombre"],
        labels=df_grouped["indicateur"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(f"Répartition des types de crimes en {annee_choisie}")
    plt.tight_layout()
    plt.show()
