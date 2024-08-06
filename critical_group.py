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



# print(prime_factor(129))





# for i in range(2, 12):
#     print(i, end=': ')
#     print(get_largest_cyclic_factor_cube(i))
for i in range(2, 12):
    print(i)
    n = i
    N = get_largest_cyclic_factor_cube(n)
    g = ncube_reduce_graph(n)
    d = Divisor(g, [N, -N] + [0]*(2*n-2))
    a = greedy(d)
    with  open("critical_group.txt", "a") as f :
        f.write(f"{i}".center(20, "=")+'\n')
        if all(i >=0 for i in a):
            f.write(str(a)+'\n')
        else:
            a = [i - min(a) for i in a]
            f.write(str(a)+'\n')

# n = 10
# g = ncube_graph(n)
# lap = g.laplacianMatrix()
# rscript = [128898, 0, 71540, 57358, 66143, 62755, 65085, 63813, 64768, 64130, 64642, 64256, 64581, 64317, 64547, 64351, 64526, 64372, 64512, 64386]
# script = [0 for i in range(g.nodenum)]

# for i in range(g.nodenum):
#     first_bit = 1 if i & (1 << (n-1)) else 0 
#     k = i & ((1 << (n-1)) - 1)

#     #count how many 1 in k
#     count = 0
#     for j in range(n):
#         if k & (1 << j):
#             count += 1

#     idx = 2*count + first_bit
#     # print(i,idx, first_bit, count,bin(k).replace('0b',''))
#     script[i] = rscript[idx]

# # exit()
# script = np.array(script).transpose()
# ans = lap @ script
# print(get_largest_cyclic_factor_cube(n))
# print(ans.min())
# print(ans.max())
# print(np.count_nonzero(ans))
# print(ans)

# for n in range(2,14):
#     print(get_largest_cyclic_factor_cube(n))
