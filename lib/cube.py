import numpy as np
from lib.graph import Graph
from lib.prime import ODD_PRIME, PRIME_FACTOR, prime_factor
from lib.algorithms import *

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
        flag = 0
        for i in range(2,n+1):
            for f,m in prime_factor(i):
                if f == p  and m > flag:
                    flag = m
        ans *= p**flag
    return ans

def ncube_reduce_graph(n: int) -> Graph:
    nk = n*2
    g = Graph(nk)
    for i in range(n):
        g.addEdge(2*i, 2*i+1,combination(n-1, i))

    for i in range(n-1):
        g.addEdge(2*i, 2*i+2,combination(n-1, i)*(n-1-i))
        g.addEdge(2*i+1, 2*i+3,combination(n-1, i)*(n-1-i))
    
    return g