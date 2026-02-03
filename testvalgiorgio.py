"""
différents graphiques :

- Nombre de crimes par type et par année

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"----------------------------------------------------------------------------------------"

"""graphique nombre de crimes par type et par année"""


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


"------------------------------------------------------------------------------"

"""
TO-DO :
 - graphique type de crime par année (camembert), ou l'utilisateur choisit l'année
 - graphique évolution d'un type de crime sur toutes les années (courbe), ou l'utilisateur choisit le type de crime
 - graphique nombre de crime par type et par année dans chaque département (batons empilés), ou l'utilisateur choisit un département

"""