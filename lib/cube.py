import numpy as np


def hammingDistance(n1, n2):

    x = n1 ^ n2
    setBits = 0

    while (x > 0):
        setBits += x & 1
        x >>= 1

    return setBits


def ncube_laplacian(n: int) -> np.ndarray:
    size = 2**n
    matrix = np.identity(size, dtype=int)
    matrix = matrix * (n)
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if hammingDistance(i, j) == 1:
                matrix[i][j] = -1
    return matrix
