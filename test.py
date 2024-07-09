from lib.graph import Graph
from lib.matrix import *
from lib.cube import *
from lib.algorithms import *
from lib.divisor import Divisor
import numpy as np

# def test():
#     N = 24
#     m = ncube_laplacian(3)
#     print(m)
#     m  = m[1:,1:]
#     m = m.astype(float)
#     invm= np.linalg.inv(m)
#     divisor = [N,-N] + [0]*(len(invm)-2)
#     ans = invm @ np.array(divisor)
#     ans = ans.astype(int)
#     print(ans)



n = 3
N = 24
g = Graph(2**n)
g.init_with_Laplacian(ncube_laplacian(n))
d = Divisor(g, [N,-N] + [0]*(2**n-2))
a = greedy(d)
if all(i >= 0 for i in a):
    print(a)
else:
    a = [i - min(a) for i in a]
    print(a)


#-----------------------

reduce_n = 2*n
reduce_g = Graph(reduce_n)
reduce_g.addEdges([(0,1),(4,5)]+[(0,2),(2,4),(1,3),(3,5),(2,3)]*2)
reduce_d = Divisor(reduce_g, [N,-N] + [0]*(reduce_n-2))

reduce_a = greedy(reduce_d)
if all(i>=0 for i in reduce_a):
    print(reduce_a)
else:
    reduce_a = [i - min(reduce_a) for i in reduce_a]
    print(reduce_a)

