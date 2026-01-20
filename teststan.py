import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("InfoCrimes.csv", sep=";")


df["annee"] = df["annee"].astype(int)
df["nombre"] = df["nombre"].astype(int)
df["Code_departement"] = df["Code_departement"].astype(str)
df["Code_region"] = df["Code_region"].astype(str)

def tableau_crimes_occurrences_par_annee(df, annee):
    filtre = df
        
    filtre = filtre[filtre["annee"] == annee]

    return (
        filtre
        .groupby("indicateur", as_index=False)["nombre"]
        .sum()
        .rename(columns={"nombre": "occurrence_totale"})
        .sort_values(by="occurrence_totale", ascending=False)
        .reset_index(drop=True)
    )

def compare_crime_annee(df, type_crime, annee1, annee2):
    pass

def tableau_crimes_occurrences(
    df,
    annee=None,
    code_departement=None,
    code_region=None,
    indicateur=None
):
    filtre = df.copy()

    if annee is not None:
        filtre = filtre[filtre["annee"] == annee]

    if code_departement is not None:
        filtre = filtre[filtre["Code_departement"] == code_departement]

    if code_region is not None:
        filtre = filtre[filtre["Code_region"] == code_region]

    if indicateur is not None:
        filtre = filtre[filtre["indicateur"] == indicateur]

    return (
        filtre
        .groupby("indicateur", as_index=False)["nombre"]
        .sum()
        .rename(columns={"nombre": "occurrence_totale"})
        .sort_values(by="occurrence_totale", ascending=False)
        .reset_index(drop=True)
    )


print(tableau_crimes_occurrences_par_annee(df, 2018))
print(tableau_crimes_occurrences(df, 2018, "74", None, "Violences sexuelles"))

#Faire un graphique extérieur à l'invite de console
#Faire en sorte que les fonctions soient plus polyvalentes : une fonction de tri qui peut faire année et département en même temps
#Commander le logiciel depuis l'interface graphique avec Tkinter
#Faire toutes les merdes : main menu etc

#Liste de fonctionnalités nécessaires :
#   -Extraire les données selon un ou plusieurs paramètres ( fonction qui renvoie les crimes commis en telle année, en tel lieu, de telle manières etc)
#   -Fonctionnalité de compraison de ces statistiques ( crimes de 2018 vs 2019 ( qui peut être combiné avec les options du dessus ) )
#   -Ergonomie maximale sur l'interface graphique en priorité par rapport à l'esthétisme