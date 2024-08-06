from lib.graph import Graph
from lib.matrix import *
from lib.cube import *
from lib.algorithms import *
from lib.divisor import Divisor
import numpy as np
from lib.prime import *
import math


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n*factorial(n-1)


def mt(n: int) -> int:
    return max(v2(x)+x for x in range(1, n))
# g = ncube_graph(3)


class FCOLOR(enumerate):
    RED = 91
    GREEN = 92
    YELLOW = 93
    BLUE = 94
    MAGENTA = 95
    CYAN = 96
    WHITE = 97


def color(str, c):
    return f"\x1b[{c}m{str}\x1b[0m"
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


load_prime()
data: dict[int, list[int]] = {}
with open("data.txt") as f:
    idx = 2
    for line in f:
        if line == '\n':
            continue
        data[idx] = list(map(int, line.strip('[]\n').split(', ')))
        idx += 1


for n, script in data.items():
    # print(n, end=': \n')
    for i in range(len(script)):
        # print(i, end=' ')
        for t, m in prime_factor(script[i]):
            c = '\x1b[91m' if m == 1 else '\x1b[92m'
            # print(f"{t}^{c}{m}\x1b[0m", end=', ')
            # print(f"{t}^{m}", end=', ')
        # print()
    # print('------------')


for n, script in data.items():
    print(n, end=': \n')
    print(script[2*n-2])
    for p, m in prime_factor(script[2*n-2]):
        c = FCOLOR.GREEN
        if p == 2:
            c = FCOLOR.RED
        print(f"{color(p,c)}^{m}", end=', ')
    print()
    print("-----------")
# for n,script in data.items():
#     print(f"{n}")
#     script.remove(0)
#     for i in range(len(script)-1):
#         print(script[i]-script[i+1], end=', ')

#     print()
#     print("-----------")

# for n,script in data.items():
#     print(f"{n}:  {get_largest_cyclic_factor_cube(n)}")
#     maxnumberlength = len(str(max(script)))
#     for i in range(0,len(script)-1,2):
#         print(f"{script[i]:<{maxnumberlength}}",end='  ')
#     print()
#     for i in range(1,len(script),2):
#         print(f"{script[i]:<{maxnumberlength}}",end='  ')
#     print()
    # for i in range(0,len(script)-1,2):
    #     print(f"\x1b[95m{script[i]-script[i+1]:<{maxnumberlength}}\x1b[0m",end='  ')
    # print()
    # print("-----------")


# for n in range(2,20):
#     print(f"{}")
#     print(get_largest_cyclic_factor_cube(n)/(n*(n-1)))
#     a = int(get_largest_cyclic_factor_cube(n)/(n*(n-1)))
#     print(prime_factor(a))
#     print("-----------")

# script3= data[3]
# g3 = ncube_reduce_graph(3)
# l3 = g3.laplacianMatrix()
# s3 = np.array([script3]).transpose()
# print(l3 @ s3)

# for n in range(2,30):
#     print(f"{n}")
#     ans =1
#     for p in ODD_PRIME:
#         if p > n:
#             break
#         flag = 0
#         for i in range(2,n+1):
#             for f,m in prime_factor(i):
#                 if f == p  and m > flag:
#                     flag = m
#         ans *= p**flag

#     lcm = math.lcm(*[i for i in range(1,n+1)])
#     print(ans)
#     ans = get_largest_cyclic_factor_cube(n)
#     print(f"\x1b[94m{ans/lcm}\x1b[0m")
#     print(prime_factor(ans))
#     print("-----------")

# g = ncube_reduce_graph(5)
# print(g.laplacianMatrix())
# print(np.delete(np.delete(g.laplacianMatrix(), 0, 0), 0, 1))


# while True:
#     x,y = (int(k) for k in input().split())
#     dcompx = prime_factor(x)
#     dcompy = prime_factor(y)
#     for f,m in dcompx:
#         print(f"{f}^{m}", end=', ')
#     print()
#     for f,m in dcompy:
#         print(f"{f}^{m}", end=', ')
#     print("\n-----------------")
