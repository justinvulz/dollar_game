from lib.graph import Graph
from lib.matrix import *

# g = Graph(3)

# g.addEdge(1, 0)
# g.addEdge(1, 2)
# g.addEdge(2, 0)

# print(g.adjMatrix())
# print(g.laplacianMatrix())


mt = np.array([[2,4,4],
               [-6,6,12],
               [10,4,16]])
mt = np.array([[2,4,6],[1,3,5]])
mbt = np.array([[4,6]])

inv = invariant_factors(mt)

print(inv)
