import pandas as pd
import matplotlib.pyplot as plt

path = '/home/matteo/Desktop/python/data/air.csv'

df = pd.read_csv(path)

# separatore corretto

df = pd.read_csv(path, sep=';')

# valori nulli 

df = pd.read_csv(path, sep=';', na_values=[-200])


# solo colonne interessate

df = pd.read_csv(
    path, 
    sep=';', 
    na_values=[-200],
    usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"]
    )

# colonne temporali

df = pd.read_csv(
    path, 
    sep=';', 
    na_values=[-200],
    usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"],
    parse_dates=[["Date", "Time"]]
)


print(df.dtypes)



df = pd.read_csv(
    path, 
    sep=';', 
    na_values=[-200],
    usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"],
    parse_dates=[["Date", "Time"]]
).rename(
    columns={
        "CO(GT)": "co",
        "Date_Time": "tstamp",
        "T": "temp_c",
        "RH": "rh",
        "AH": "ah"
    }
)

df["tstamp"] = pd.to_datetime(df["tstamp"], format="%d/%m/%Y %H.%M.%S")
df.set_index("tstamp", inplace=True) 

# date minime e massime
df.index.min()
df.index.max()

# estrazione giorno settimana
df.index.day_name()


# aggregazione giorno settimana media co
df.groupby(df.index.day_name())["co"].mean()

df.groupby(df.index.day_name())["co"].mean().sort_values(ascending=False)
df.groupby(df.index.day_name())["co"].mean().sort_values(ascending=True)

risultati = df.groupby(df.index.day_name())["co"].mean().sort_values(ascending=True)


# aggregazione multipla
df.groupby([df.index.day_name(), df.index.hour])["co"].mean()


# funzione resample
df.resample("M")["co"].agg(["mean"])


df.plot()
plt.show()

df.plot(y="co")
plt.show()

df.plot(y=["rh", "ah"])
plt.show()


risultati = df.groupby(df.index.day_name())["co"].mean()
risultati.plot(kind='bar')
plt.show()


risultati.plot(kind='bar', color='red')
plt.show()

df.groupby(df.index.day_name())["co"].mean().plot()
plt.show()