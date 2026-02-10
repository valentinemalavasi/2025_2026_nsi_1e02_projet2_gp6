import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lecture du CSV
df = pd.read_csv("InfoCrimes.csv", sep=";")

# Conversion des colonnes numériques
df["annee"] = pd.to_numeric(df["annee"], errors="coerce")
df["nombre"] = pd.to_numeric(df["nombre"], errors="coerce")

# ===== Choix du département =====
departement = input("Entrez le code du département (ex : 01) : ")

# Filtrage sur le département
df_dep = df[df["Code_departement"] == departement]

# Vérification
if df_dep.empty:
    print(f"Aucune donnée disponible pour le département {departement}.")
else:
    # Agrégation : somme des crimes par année et type
    df_counts = (
        df_dep.groupby(["annee", "indicateur"])["nombre"]
        .sum()
        .reset_index()
    )

    # Pivot pour le graphique
    df_pivot = df_counts.pivot(
        index="annee",
        columns="indicateur",
        values="nombre"
    ).fillna(0)

    # Graphique
    fig, ax = plt.subplots(figsize=(12, 6))
    df_pivot.plot(kind="bar", stacked=True, ax=ax)

    ax.set_xlabel("Année")
    ax.set_ylabel("Nombre de crimes")
    ax.set_title(f"Nombre de crimes par type et par année\nDépartement {departement}")
    ax.legend(title="Type de crime", bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.show()
