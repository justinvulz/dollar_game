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

S = smith_normal_form(mt)

print(S)

print(mt)