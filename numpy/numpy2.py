import numpy
vector = numpy.array([5, 10, 15, 20])
print(vector == 10)
print(vector)

equal_to_ten_and_five = (vector == 10) & (vector == 5)
print(equal_to_ten_and_five)

equal_to_ten_or_five = (vector == 10) | (vector == 5)
print(equal_to_ten_or_five)

print("-----------------")

matrix = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

print(matrix == 25)

second_column_25 = (matrix[:, 1] == 25)
print(second_column_25)
print(matrix[second_column_25, :])

print("------------------")

vector1 = numpy.array(["1", "2", "3"])
print(vector1.dtype)
print(vector1)
vector1 = vector1.astype(float)
print(vector1.dtype)
print(vector1)

vector2 = numpy.array([5, 10, 15, 20])
print(vector.min())


print(matrix.sum(axis = 1))

print(matrix.sum(axis = 0))

print("-------------------")

world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",",dtype=float)
print(world_alcohol)
