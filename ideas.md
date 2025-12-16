print("=== FILTRE DE RECHERCHE CRIMES ===")
print("Laissez vide si vous ne voulez pas filtrer cette catégorie.\n")

# Demander les filtres à l'utilisateur (tous optionnels)
filtres = {
    "Code_departement": input("Code département : ").strip(),
    "Code_region": input("Code région : ").strip(),
    "annee": input("Année : ").strip(),
    "indicateur": input("Type de crime (ex: Homicides) : ").strip(),
    "unite_de_compte": input("Unité de compte : ").strip(),
    "nombre": input("Nombre exact : ").strip(),
    "taux_pour_mille": input("Taux pour mille : ").strip(),
    "insee_pop": input("INSEE population : ").strip(),
    "insee_pop_millesime": input("INSEE population millésime : ").strip(),
    "insee_log": input("INSEE logements : ").strip(),
    "insee_log_millesime": input("INSEE logements millésime : ").strip(),
}

# Appliquer les filtres — seulement ceux remplis
df_filtre = df.copy()

for colonne, valeur in filtres.items():
    if valeur != "":
        # Si valeur peut être un nombre, on cast automatiquement
        try:
            valeur = float(valeur) if "." in valeur else int(valeur)
        except:
            pass  # valeur reste un texte

        df_filtre = df_filtre[df_filtre[colonne] == valeur]

# Afficher le résultat
print("\n=== RÉSULTATS TROUVÉS ===")
if df_filtre.empty:
    print("Aucun résultat ne correspond aux filtres.")
else:
    print(df_filtre)