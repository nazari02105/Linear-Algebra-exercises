import numpy as np

def row_reduced_echelon(A, Z = None):
    r, c = A.shape
    if r == 0 or c == 0:
        return A
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        B = row_reduced_echelon(A[:,1:])
        return np.hstack([A[:,:1], B])
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row
    D = (np.matrix(Z)).I if Z is not None else None
    A[1:] -= A[0] * A[1:,0:1]
    B = row_reduced_echelon(A[1:,1:])
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ]) if D is None else D

n = int(input())
main_list = []
for i in range(n):
    main_list.append(list(map(int, input().split())))
    
I = np.eye(n)
main_list = np.asarray(main_list)
main_list_2 = np.hstack((main_list, I))

rref = row_reduced_echelon(main_list_2, main_list)
rref = ((np.array(rref)).round()).astype(int)
rref = rref.tolist()
for i in rref:
    print(" ".join(map(str, i)))
