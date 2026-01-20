import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("InfoCrimes.csv", sep=";")

def crimes_par_annee(df, annee):
    crimes = df[df["annee"] == annee]["indicateur"]
    return crimes.unique().tolist()

crimes_2018 = crimes_par_annee(df, 2018)
print(crimes_2018)