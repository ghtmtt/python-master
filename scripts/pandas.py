import pandas as pd

# Series

# s = pd.Series(data, index)

i = [1, 2, 3]
l = ['a', 'b', 'c']

s = pd.Series(l, i)

# stampa Series
s

# ricavare indice
s.index

# trasformare indice in lista
idx = list(s.index)

# estrazione elementi
s[1]

# operazioni su Series
ss = s + s

# DataFrame

l = [1, 2, 3, 4]

# creazione dataframe da lista
df = pd.DataFrame(l)

df

# creazione dataframe da dizionario
d = {'uno': [1,2,3], 'due': [4,5,6], 'tre': [7,8,9]}

df = pd.DataFrame(d)

df

# estrazione con nome colonna
df['due']

# aggiunta colonna
df['quattro'] = [10, 11, 12]

df['cinque'] = df['uno'] + df['quattro']

# eliminazione colonna
del df['cinque']

# valori ripetuti
df['sei'] = 6

# sostituzione singolo valore
df['tre'][1] = 100

# estrazione indice
df.index

# riassegnazione valori indice
df.index = ['00', '11', '22']

# estrazione righe
df.iloc[0:2]

# estrazione riga da valore indice
df.loc['00']

# rinominare colonna
df.rename(columns={'sei': 'cinque'}, inplace=True)


