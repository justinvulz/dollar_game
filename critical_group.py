from lib.cube import *
from lib.matrix import *
from lib.graph import Graph
from lib.divisor import Divisor
import numpy as np
from lib.algorithms import *

# for i in range(2,15):
#     # l = ncube_laplacian(i)
#     # print(i, end=': ')
#     # print(invariant_factors(l[1:, 1:]))
#     print(f"{i:<3}",get_largest_cyclic_factor_cube(i))




def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n*factorial(n-1)


def combination(n: int, k: int) -> int:
    return factorial(n)//(factorial(k)*factorial(n-k))


def test(n: int) -> Graph:
    nk = n*2
    g = Graph(nk)
    for i in range(n):
        g.addEdge(2*i, 2*i+1,combination(n-1, i))

    for i in range(n-1):
        g.addEdge(2*i, 2*i+2,combination(n-1, i)*(n-1-i))
        g.addEdge(2*i+1, 2*i+3,combination(n-1, i)*(n-1-i))
    
    return g



# for i in range(2, 8):
#     print(f"{i}".center(20, "="))
#     n = i
#     N = get_largest_cyclic_factor_cube(n)
#     g = ncube_graph(n)
#     d = Divisor(g, [N, -N] + [0]*(2**n-2))
#     a = greedy(d)
#     if all(i >= 0 for i in a):
#         print(a)
#     else:
#         a = [i - min(a) for i in a]
#         print(a)

f = open("critical_group.txt", "w")

for i in range(2, 13):
    print(i)
    print(f"{i}".center(20, "="), file=f)
    n = i
    N = get_largest_cyclic_factor_cube(n)
    g = test(n)
    d = Divisor(g, [N, -N] + [0]*(2**n-2))
    a = greedy(d)
    if all(i >=0 for i in a):
        print(a, file=f)
    else:
        a = [i - min(a) for i in a]
        print(a, file=f)
