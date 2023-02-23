import numpy as np

N, M, K = list(map(int, input().split()))
main_matrix = []
for _ in range(M):
    main_matrix.append(list(map(float, input().split())))
main_matrix = (np.matrix(main_matrix)).I.T

for _ in range(K):
    point = list(map(float, input().split()))
    point = np.array(point)
    result = np.dot(main_matrix, point)
    result = np.sum(result)
    # print(result)
    result = np.around(result, decimals=10)
    if result == 1.0:
        print("YES")
    else:
        print("NO")
    # print("-------------------------")
