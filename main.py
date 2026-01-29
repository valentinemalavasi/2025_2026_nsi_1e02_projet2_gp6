import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df = pd.read_csv("InfoCrimes.csv", sep=";")
df_optimised = df.iloc [:, [0, 1 ,2 ,3, 4, 5, 8]]
print(df_optimised)


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

print(tableau_crimes_occurrences(df, 2019)) #changer l'année pour les infos crimes des autres années




"""=========================================================================================================================================================================================="""
#idée graphique

departement = df.iloc [:, [0]]
info_crime = {
    'Nombre de victimes': df.iloc [:, [5]],
    'Année': df.iloc [:, [2]],
    'Taux pour mille': df.iloc [:, [6]],
}

x = np.arange(len(departement))  # the label locations
width = 0.25                 
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in info_crime.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# associe un texte aux axes
ax.set_ylabel('Nombre de victimes')
ax.set_title('Années')
ax.set_xticks(x + width, departement)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

plt.show()


annees = []
annees_triees = sorted(annees)
print(annees_triees)
[]


"""===================================================================================================================================================================================="""

"NOUVELLE VERSION CHATGPT"

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("InfoCrimes.csv", sep=";")

if "count" not in df.columns:
    df_counts = df.groupby(["annee", "indicateur"]).size().reset_index(name="count")
else:
    df_counts = df.groupby(["annee", "indicateur"])["count"].sum().reset_index()


df_pivot = df_counts.pivot(index="annee", columns="indicateur", values="count").fillna(0)

fig, ax = plt.subplots(figsize=(12, 6))

df_pivot.plot(kind='bar', stacked=True, ax=ax)

ax.set_xlabel("Année")
ax.set_ylabel("Nombre de crimes")
ax.set_title("Nombre de crimes par type et par année")
ax.legend(title="Type de crime")

plt.tight_layout()
plt.show()