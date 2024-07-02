from lib.graph import Graph
from lib.matrix import *
from lib.cube import *
import sys
import cProfile
# g = Graph(3)

# g.addEdge(1, 0)
# g.addEdge(1, 2)
# g.addEdge(2, 0)

# print(g.adjMatrix())
# print(g.laplacianMatrix())

np.set_printoptions(linewidth=5000)
np.set_printoptions(threshold=np.inf)
sys.set_int_max_str_digits(10000)
mt = np.array([
    [2, -1, 0, -1, 0, 0],
    [-1, 4, -1, -1, -1, 0],
    [0, -1, 2, 0, -1, 0],
    [-1, -1, 0, 4, -1, -1],
    [0, -1, -1, -1, 4, -1],
    [0, 0, 0, -1, -1, 2]
], dtype=int)
mt = np.array([
    [3, -1, -1, -1],
    [-1, 2, 0, -1],
    [-1, 0, 2, -1]
], dtype=int)
mt = np.array([
    [2,4,4],
    [6,8,10],
    [12,16,20]
], dtype=int)
# mt = np.array([
#     [3, -1, -1, -1],
#     [-1, 2, 0, -1],
#     [-1, 0, 2, -1],
#     [-1, -1, -1, 3]
# ])
# mt = np.array([[12, 6, 4], [3, 9, 6], [2, 16, 14]], dtype=int)
# print(invariant_factors(mt))
ncubeRL = ncube_laplacian(3)
s = 2**3
# print(ncubeRL)
# print(ncubeRL[:s-1, :s-1])
# print(invariant_factors(ncubeRL))
print(invariant_factors(ncubeRL[:s-1, :s-1]))
# def test():
#     for i in range(2, 7):
#         print(i, end=': ')
#         # invariant_factors(ncube_laplacian(i)[1:, 1:])
#         print(invariant_factors(ncube_laplacian(i)[1:, 1:]))
# test()