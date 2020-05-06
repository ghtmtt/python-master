import numpy as np
import matplotlib.pyplot as plt

# differenza lista e array

a = np.array([1,2,3])
m = np.array([ [1,2,3], [4,5,6], [7,8,9] ])

a[0]
m[0][0]

i = np.ones(10)
i0 = np.zeros(5)

am = np.arange(1, 10, 1)
am2 = np.arange(1, 10, .5)

ln = np.linspace(1, 10, 5)
ln2 = np.linspace(1, 10, 8)


a.ndim
m.ndim

a.size
m.size

a.shape
m.shape


m1 = np.arange(1, 10, 1)
m1 = m1.reshape(3, 3)

m1 > 6
m1[m1 > 6]


n1 = np.array([1,2])
n2 = np.array([10, 10])

n1 + 50

n3 = np.arange(1, 100, 2)

n3.max()
n3.min()
n3.sum()

nm = np.array([[10, 20, 40], [50, 12, 56]])
nm.sum()
nm.min()

nm1 = np.array([[10, 20, 40], [50, 12, 56], [100, 34, 78]])
nm1.transpose()


mu = 1
sigma = 0.5

v = np.random.normal(mu, sigma, 10000)

plt.hist(v, bins=50, density=1)
plt.show()

