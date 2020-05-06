import os
import pandas as pd

# file = os.path.join(
#    os.path.dirname(os.path.realpath(__file__)),
#    '..',
#    'data',
#    'natural_disaster.csv' 
# )

file = r'/home/matteo/Desktop/python/data/natural_disasters.csv'

df = pd.read_csv(file)

# interrogazione dataframe risultati booleani
df["Entity"] == 'Flood'

# interrograzione dataframe risultati veri
df[df["Entity"] == 'Flood']

df[(df["Entity"] == "Flood") & (df["Year"] >= 1950)]

df[(df["Entity"] == 'Flood') | (df["Entity"] == 'Landslide')]

# primi metodi del dataframe

df.describe()

df["Deaths"].describe()

df[["Deaths", "Year"]].describe()

df["Deaths"].sum()
df["Deaths"].max()

idx = df["Deaths"].idxmax()
df.iloc[idx]

df.size
df.shape

# funzione groupby

df.groupby("Entity")["Deaths"].mean()

df[df["Year"] >= 1950].groupby("Entity")["Deaths"].mean()

df[df["Entity"] == 'Earthquake'].groupby("Entity")["Deaths"].mean()
df[df["Entity"] == 'Earthquake'].groupby("Entity")["Deaths"].max()
df[df["Entity"] == 'Earthquake'].groupby("Entity")["Deaths"].sum()

df[
    (df["Entity"] == 'Earthquake') &
    (df["Year"] >= 1950) &
    (df["Year"] < 1990)
].groupby("Entity")["Deaths"].sum()


terremoti = df[
    (df["Entity"] == 'Earthquake') &
    (df["Year"] >= 1950) &
    (df["Year"] < 1990)
]

terremoti["Deaths"].sum()