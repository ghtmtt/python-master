import datetime

adesso = datetime.datetime.now()

print(adesso)

adesso_data = datetime.date.today()

# adesso_tempo = datetime.time

data = datetime.date(2020, 5, 4)

# modo selettivo
# from datetime import datetime, date, time

# adesso = datetime.now()

# timestamp numero di secondi dal 1 gennaio 1970 UTC


mese = data.month

data_dt = datetime.datetime(2020, 5, 5, 22, 35, 32)
data_dt.hour

# timedelta

d1 = datetime.date(2020, 5, 5)
d2 = datetime.date(2018, 4, 15)

dd = d1 - d2

dd1 = d2 - d1


data_stringa = '4/5/2020'
data_stringa_convertita = datetime.datetime.strptime(data_stringa, "%d/%m/%Y")

print(type(data_stringa))
print(type(data_stringa_convertita))

print(data_stringa_convertita.strftime("%Y"))
