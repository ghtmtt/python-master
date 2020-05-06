import wikipedia as wp
import pandas as pd
import matplotlib.pyplot as plt

p = 'List of selfie-related injuries and deaths'

html = wp.page(p).html().encode("UTF-8")

df = pd.read_html(html)

df = df[0]

df.describe()

df["Casualties"].sum()

gp = df.groupby("Country")["Casualties"].sum()
gp = df.groupby("Country")["Casualties"].sum().sort_values(ascending=False)

df.groupby("Type")["Casualties"].sum().sort_values(ascending=False)

gpi = df.groupby(["Country", "Type"])["Casualties"].sum()

gpi.index

gpi["India"]
gpi["India", "Animal"]

gpi.plot()
plt.show()

gpi["India"].plot()
plt.show()

gpi["India"].plot(kind='bar')
plt.show()

gpi["United States"].plot(kind='bar')
plt.show()
