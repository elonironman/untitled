import numpy

vector = numpy.array([1, 2, 3, 4])
print(vector.shape)
#This is vector, not matrix

matrix = numpy.array([[5, 10, 15], [20, 25, 30]])

print(matrix.shape)

world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",", dtype=str, skip_header=1)
#print(world_alcohol)

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]

print(uruguay_other_1986)
print(third_country)

vector1 = numpy.array([5, 10, 15, 20])
print(vector1[0:3])

matrix1 = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
print(matrix1[:, 1])

print(matrix1[:, 0:2])

print(matrix1[1:3, 0:2])