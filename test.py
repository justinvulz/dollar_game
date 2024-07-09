from lib.graph import Graph
from lib.matrix import *
from lib.cube import *
import numpy as np

def test():
    N = 24
    m = ncube_laplacian(3)
    print(m)
    m  = m[1:,1:]
    m = m.astype(float)
    invm= np.linalg.inv(m)
    divisor = [N,-N] + [0]*(len(invm)-2)
    ans = invm @ np.array(divisor)
    ans = ans.astype(int)
    print(ans)

g = Graph(ncube_laplacian(3))
print(g.get_invariant_factors())


# test()