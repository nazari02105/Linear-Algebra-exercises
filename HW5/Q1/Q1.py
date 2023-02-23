import numpy as np


def eig_vals(A: np.matrix, iter: int) -> np.array:
    to_return = A
    for _ in range(iter):
        in_q, in_r = np.linalg.qr(to_return)
        to_return = in_r * in_q
    return to_return


x = input()
my_matrix = np.matrix(x)
hello = eig_vals(my_matrix, 1000)
hello = np.diag(hello)
hello = np.sort(hello)
hello = np.flip(hello)
result = ""
for i in hello:
    now = np.round(i, 2)
    formatted_float = "{:.2f}".format(now)
    result += formatted_float + " "
result = result.strip()
print(result)
