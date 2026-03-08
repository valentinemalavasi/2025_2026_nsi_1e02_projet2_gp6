import pandas as pd

def charger_donnees():
    try:
        return pd.read_csv("InfoCrimes.csv", sep=";")
    except:
        return None

def filtrer_donnees(donnees, annee, type_crime, departement):
    df = donnees.copy()

    if annee != "Toutes":
        df = df[df["annee"] == int(annee)]

    if type_crime != "Tous":
        df = df[df["indicateur"] == type_crime]

    if departement != "Tous":
        df = df[df["Code_departement"] == departement]

    return df

def data_evolution(df):
    return df.groupby("annee")["nombre"].sum().reset_index()

def data_repartition(df):
    data = df.groupby("indicateur")["nombre"].sum().reset_index()
    return data.sort_values("nombre", ascending=False).head(10)