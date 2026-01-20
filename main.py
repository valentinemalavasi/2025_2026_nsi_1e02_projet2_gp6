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

print(tableau_crimes_occurrences(df, 2018))





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

def crimes_par_annee(df, annee):
    crimes = df[df["annee"] == annee]["indicateur"]
    return crimes.unique().tolist()

crimes_2018 = crimes_par_annee(df, 2018)
print(crimes_2018)

# import matplotlib.pyplot as plt
# import numpy as np

# species = ("Adelie", "Chinstrap", "Gentoo")
# penguin_means = {
#     'Bill Depth': (18.35, 18.43, 14.98),
#     'Bill Length': (38.79, 48.83, 47.50),
#     'Flipper Length': (189.95, 195.82, 217.19),
# }

# x = np.arange(len(species))  # the label locations
# width = 0.25  # the width of the bars
# multiplier = 0

# fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in penguin_means.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     ax.bar_label(rects, padding=3)
#     multiplier += 1

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Length (mm)')
# ax.set_title('Penguin attributes by species')
# ax.set_xticks(x + width, species)
# ax.legend(loc='upper left', ncols=3)
# ax.set_ylim(0, 250)

# plt.show()
