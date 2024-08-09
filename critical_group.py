from lib.cube import *
from lib.matrix import *
from lib.graph import Graph
from lib.divisor import Divisor
import numpy as np
from lib.algorithms import *

for n in range(3,7):
    g = ncube_graph(n)
    l = g.laplacianMatrix()
    print(n, end=': ')
    # print(invariant_factors(l[1:, 1:]))
    print(np.linalg.det(l[1:, 1:]))
    print("===")

for n in range(3,7):
    g = ncube_reduce_graph(n)
    l = g.laplacianMatrix()
    print(n, end=': ')
    # print(np.linalg.det(np.delete(np.delete(l, 1, 0), 1, 1)))
    print(np.linalg.det(l[1:, 1:]))
    print("===")