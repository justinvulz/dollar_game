import numpy as np
from lib.graph import Graph


PRIME_FACTOR = {
    2 : [2],
    3 : [3],
    4 : [4],
    5 : [5],
    6 : [2,3],
    7 : [7],
    8 : [8],
    9 : [9],
    10 : [2,5],
    11 : [11],
    12 : [4,3],
    13 : [13],
    14 : [2,7],
    15 : [5,3],
    16 : [16],
    17 : [17],
    18 : [9,2],
    19 : [19],
    20 : [5,4],
    21 : [7,3],
}
ODD_PRIME = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
PRIME = [2] + ODD_PRIME


def hammingDistance(n1, n2):

    x = n1 ^ n2
    setBits = 0

    while (x > 0):
        setBits += x & 1
        x >>= 1

    return setBits


def ncube_graph(n: int) -> Graph: 
    size = 2**n
    matrix = np.identity(size, dtype=int)
    matrix = matrix * (n)
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if hammingDistance(i, j) == 1:
                matrix[i][j] = 1
    g = Graph(len(matrix))
    for i in range(g.nodenum):
        for j in range(i,g.nodenum):
            if  matrix[i][j] :
                g.addEdge(i, j)

    return g

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


def get_largest_cyclic_factor_cube(n: int) -> int:
    ans = 2**v2_largest_cyclic_factor_cube(n)
    for p in ODD_PRIME:
        if p > n:
            break
        flag =1
        for i in range(2,n+1):
            for f in PRIME_FACTOR[i]:
                if f%p ==0 and f > flag:
                    flag =f
        ans *= flag
    return ans
