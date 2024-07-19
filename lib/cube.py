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

def v2(x)  -> int:
    n = 0
    while x%2 == 0:
        n += 1
        x = x//2
    return n

def v2_largest_cyclic_factor_cube(n: int) -> int:
    u = max(v2(x)+x for x in range(1,n))
    u = max(u, v2(n)+n-1)
    return u