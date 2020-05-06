import pandas as pd

p_d1 = '/home/matteo/Desktop/python/data/d1.csv'
p_d2 = '/home/matteo/Desktop/python/data/d2.csv'
p_d3 = '/home/matteo/Desktop/python/data/d3.csv'

d1 = pd.read_csv(p_d1)
d2 = pd.read_csv(p_d2)
d3 = pd.read_csv(p_d3)

# merge
d1.merge(d2, left_on="Code", right_on="Code")

dm = d1.merge(d2, left_on="Code", right_on="Code")

dm = d1.merge(d2, left_on="Code", right_on="Code", suffixes=('_left', '_right'))
dm = d1.merge(d2, left_on="Code", right_on="Code", suffixes=('', '_right'))

d1.set_index("Code", inplace=True)
d2.set_index("Code", inplace=True)
d3.set_index("Code", inplace=True)

d1.merge(d2)

d1.merge(d3)
dmn = d1.merge(d3, how='left')

