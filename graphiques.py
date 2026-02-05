"""
différents graphiques :

- Nombre de crimes par type et par année
- Graphique type de crime par année (camembert), ou l'utilisateur choisit l'année
- Graphique nombre de crime par type et par année dans un département ou l'utilisateur choisit le département
- Graphique évolution d'un type de crime en fonction du temps en années (courbe), ou l'utilisateur choisit le type de crime dont il veut voir l'évolution

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"--------------------------------------------------------------------------------------------------------------"

"graphique nombre de crimes par type et par année"
"""
# Lecture du CSV
df = pd.read_csv("InfoCrimes.csv", sep=";")

# Conversion de la colonne "nombre" en numérique
df["nombre"] = pd.to_numeric(df["nombre"], errors="coerce")

# Agrégation : somme des crimes par année et indicateur
df_counts = (
    df.groupby(["annee", "indicateur"])["nombre"]
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
ax.set_title("Nombre de crimes par type et par année")
ax.legend(title="Type de crime")

plt.tight_layout()
plt.show()


"-------------------------------------------------------------------------------------------------------------"

"graphique type de crime par année (camembert), ou l'utilisateur choisit l'année"

# Lecture du CSV
df = pd.read_csv("InfoCrimes.csv", sep=";")

# Conversion des colonnes numériques
df["annee"] = pd.to_numeric(df["annee"], errors="coerce")
df["nombre"] = pd.to_numeric(df["nombre"], errors="coerce")

# ===== Année choisie par l'utilisateur =====
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

"---------------------------------------------------------------------------------------------------------------"

"graphique nombre de crime par type et par année dans un département ou l'utilisateur choisit le département"

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
"""
"--------------------------------------------------------------------------------------------------------------"

"graphique évolution d'un type de crime en fonction du temps en années (courbe), ou l'utilisateur choisit le type de crime dont il veut voir l'évolution"

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

"------------------------------------------------------------------------------------"

"""
TO-DO :
 OK- graphique type de crime par année (camembert), ou l'utilisateur choisit l'année 
 OK- graphique évolution d'un type de crime sur toutes les années (courbe), ou l'utilisateur choisit le type de crime
 OK- graphique nombre de crime par type et par année dans chaque département (batons empilés), ou l'utilisateur choisit un département
 -préciser les différents crimes dans le input du graphique ou l'utilisateur choisit le type de crime
 -pareil pour les dépatartements

"""