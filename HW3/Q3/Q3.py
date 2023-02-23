import numpy as np
import sys

np.set_printoptions(formatter={'float': '{:.1f}'.format}, threshold=sys.maxsize)

N = int(input())
main_list = []
for i in range(N):
    main_list.append(list(map(float, input().split())))
main_list = np.array(main_list)
radians = list(map(float, input().split()))
RX = np.array([[1, 0, 0], [0, np.cos(radians[0]), -np.sin(radians[0])], [0, np.sin(radians[0]), np.cos(radians[0])]])
RY = np.array([[np.cos(radians[1]), 0, np.sin(radians[1])], [0, 1, 0], [-np.sin(radians[1]), 0, np.cos(radians[1])]])
RZ = np.array([[np.cos(radians[2]), -np.sin(radians[2]), 0], [np.sin(radians[2]), np.cos(radians[2]), 0], [0, 0, 1]])

result_list = []
for i in main_list:
    for_result = RX.dot(i)
    for_result = RY.dot(for_result)
    for_result = RZ.dot(for_result)
    result_list.append(for_result)
result_list = np.array(result_list)
print(np.around(result_list, decimals=1))
