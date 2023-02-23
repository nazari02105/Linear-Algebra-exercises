import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

first_vector = np.array(list(map(int, input().split())))
second_vector = np.array(list(map(int, input().split())))
number_of_sums = len(first_vector) + len(second_vector) - 1
result = np.outer(first_vector, second_vector)
the_big_list = [0 for _ in range(number_of_sums)]
counter = -1
for i in result:
    counter += 1
    second_counter = counter
    for j in i:
        the_big_list[second_counter] += j
        second_counter += 1
print(np.array(the_big_list))
