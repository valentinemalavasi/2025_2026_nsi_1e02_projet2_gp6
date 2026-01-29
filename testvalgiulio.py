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

print(tableau_crimes_occurrences(df, 2019)) 


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