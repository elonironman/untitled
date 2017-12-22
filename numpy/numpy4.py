import numpy as np
B = np.arange(3)
print(B)
print(np.exp(B))
print(np.sqrt(B))

a = np.floor(10*np.random.random((3, 4)))
print(a)
print("-------------------")
print(a.ravel())
print("-------------------")
a.shape = (6, 2)
print(a)
print("--------------------")
print(a.T)

a = np.floor(10*np.random.random((2, 2)))
b = np.floor(10*np.random.random((2, 2)))
print(a)
print(b)
print(np.vstack((a, b)))

a = np.arange(12)
b = a

print(b is a)
b.shape = 3, 4
print(a.shape)

c = a.view()
print(c is a)
c.shape = 2, 6
print(a.shape)
c[0, 4] = 1234
print(c)
print(a)

#??? why

d = a.copy()
print(d is a)
d[0, 0] = 9999
print(d)
print(a)

