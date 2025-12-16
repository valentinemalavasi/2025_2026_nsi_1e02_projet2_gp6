import pandas as pd

# Charger les données
df = pd.read_csv("InfoCrimes.csv", sep=";")
# print(df)
df = df.iloc [:, [0, 1 ,2 ,3, 4, 5, 8]]
print(df)