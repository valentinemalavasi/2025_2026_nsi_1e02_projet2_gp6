import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("InfoCrimes.csv", sep=";")

def crimes_par_annee(df, annee):
    crimes = df[df["annee"] == annee]["indicateur"]
    return crimes.unique().tolist()

crimes_2018 = crimes_par_annee(df, 2018)
print(crimes_2018)

def tableau_crimes_occurrences(df, annee):
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

print(tableau_crimes_occurrences(df, 2019))