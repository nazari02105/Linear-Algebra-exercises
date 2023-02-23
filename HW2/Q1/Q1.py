import numpy as np

k, m, n = [int(y) for y in input().split()]

voted_coordinates = []
for i in range(m):
    line_m = [float(y) for y in input().split()]
    voted_coordinates.append(line_m)

voted_coordinates = np.asarray(voted_coordinates)

votes = [int(y) for y in input().split()]

result = ""
for i in range(n):
    line_n = np.asarray([float(y) for y in input().split()])
    voted_coordinates_copy = np.sum((np.copy(voted_coordinates) - line_n) ** 2, axis=1)
    voted_coordinates_copy = np.argsort(voted_coordinates_copy)[:k]
    my_list = [votes[index] for index in voted_coordinates_copy]
    counts = np.bincount(my_list)
    result += str(np.argmax(counts)) + " "

result = result.strip()
print(result)
