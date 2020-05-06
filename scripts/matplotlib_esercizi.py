import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()
fig.show()

# print(type(ax))

x = [1, 2, 3]
y = [4, 5, 6]

fig, ax = plt.subplots()
ax.scatter(x=x, y=y)
fig.show()

fig, ax = plt.subplots()
ax.scatter(x=x, y=y, marker='v', c='r', edgecolor='b')
fig.show()

# multi axes (grafici)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

xx = [10, 20, 30]
yy = [22, 33, 44]

n = ['A', 'B', 'C']
v = [120, 150, 180]

ax1.scatter(x=xx, y=yy)
ax2.bar(x=n, height=v, width=.5)

fig.show()


iris_p  = '/home/matteo/Desktop/python/data/iris.csv'

df = pd.read_csv(iris_p)


fig, ax = plt.subplots()
ax.scatter(x=df["sepal_width"], y=df["sepal_length"], c='red', label='sepal')
ax.scatter(x=df["petal_width"], y=df["petal_length"], c='blue', label='petal')
ax.legend()
# fig.show()

fig.savefig('/home/matteo/Desktop/python/grafico.png')
fig.savefig('/home/matteo/Desktop/python/grafico.svg')

