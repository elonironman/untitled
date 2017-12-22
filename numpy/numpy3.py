import numpy as np
print(np.arange(15))
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.size)

print(np.zeros((3,4)))

print(np.ones((2,3,4), dtype=np.int32))

print(np.arange(10, 30, 5))

print(np.arange(0, 2, 0.3))

print(np.arange(12).reshape(4, 3))

print(np.random.random((2, 3)))