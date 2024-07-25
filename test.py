from lib.graph import Graph
from lib.matrix import *
from lib.cube import *
from lib.algorithms import *
from lib.divisor import Divisor
import numpy as np
import math

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n*factorial(n-1)
def mt(n: int) -> int:
    return  max(v2(x)+x for x in range(1,n))
# g = ncube_graph(3)


# l = g.laplacianMatrix()

# script = [[14, 0, 9, 5, 9, 5, 8, 6]]
# s = np.array(script).transpose()
# print(l @ s)
# for i in range(2,6):
#     g = ncube_graph(i)
#     l = g.laplacianMatrix()
#     print(i, end=': ')
#     print(invariant_factors(l[1:, 1:]))
#     print(mt(i))
#     print("===")

for n in range(2,11):
    print(n, end=': \n')
    for k in range(0,n-1):
        upper = factorial(n-1)
        lower = factorial(k)*factorial(n-2-k)
        print(upper//lower, end=' ')
    print("\n ========")