from lib.graph import Graph
from lib.matrix import *
from lib.cube import *
from lib.algorithms import *
from lib.divisor import Divisor
import numpy as np
from lib.prime import *
import math
import decimal


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


# for n, script in data.items():
#     print(n, end=': \n')
#     print(script[2*n-2])
#     for p, m in prime_factor(script[2*n-2]):
#         c = FCOLOR.GREEN
#         if p == 2:
#             c = FCOLOR.RED
#         print(f"{color(p,c)}^{m}", end=', ')
#     print()
#     print("-----------")

# for n,script in data.items():
#     print(n, end=': \n')
#     print(get_largest_cyclic_factor_cube(n))
#     print(script[2*n-1] + (n-1)*script[2*n-4])

# for n,script in data.items():
#     print(n, end=': \n')
#     N = get_largest_cyclic_factor_cube(n)

#     print(script[0])
#     print((1+1/n)*N - (n-1) * script[2*n-4])
#     print((2)*(N + (N//n))//(n+1))

#     print("-----------")

# for n, script in data.items():
#     if n == 2:
#         continue
#     print(n, end=': \n')

#     pm1 = prime_factor(data[n-1][0])
#     pm2 = prime_factor(script[2*n-1])
#     for p in PRIME:
#         if any(t == p for t, m in pm1) or any(t == p for t, m in pm2):
#             if any(t == p for t,m in pm1) : 
#                 m = next(filter(lambda x: x[0] == p, pm1))[1]
#                 print(f"{p:>3}^{m}", end='  ')
#             else: 
#                 print(f"{' ':>5}", end='  ')
#             if any(t == p for t,m in pm2) :
#                 m = next(filter(lambda x: x[0] == p, pm2))[1]
#                 print(f"{p:>3}^{m}", end='  ')
#             print()
#     print()
#     print("-----------")

# for n, script in data.items():
#     if n== 2:
#         continue
#     print(n, end=': \n')
#     c = data[n-1][0] * (n-1) / script[2*n-1]
#     print(int(c))
#     for p,m in (prime_factor(int(c))):
#         print(f"{p}^{m}", end=', ')
#     print()
#     print("-----------")

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
#     for i in range(0,len(script)-1,2):
#         print(f"\x1b[95m{script[i]-script[i+1]:<{maxnumberlength}}\x1b[0m",end='  ')
#     print()
#     print("-----------")


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



for n,script in data.items():
    if n> 6:
        break
    g = ncube_reduce_graph(n)
    l = g.laplacianMatrix()
    rl = np.delete(np.delete(l, 1, 0), 1, 1)
    N = get_largest_cyclic_factor_cube(n)
    v = np.array([N] + [0]*(2*n-2)).transpose()
    rll = rl.copy()
    rll[:,2*n-3] = v
    print(n, end=': ')
    print(script[2*n-2])
    print(np.linalg.det(rll))
    print(np.linalg.det(rl))
    print(np.linalg.eigvals(rll))
    print(np.linalg.eigvals(rl))
    print(rll)
    print(l)
    print("--------------")  


# for n,script in data.items():
#     if n > 6:
#         break
#     g =  ncube_graph(n)
#     l = g.laplacianMatrix()
#     N = get_largest_cyclic_factor_cube(n)
#     v = np.array([N] + [0]*(2**(n)-2)).transpose()
#     rl = np.delete(np.delete(l, 1, 0), 1, 1)
#     rll = rl.copy()
#     rll[:,2**(n)-3] = v
#     print(n, end=': ')
#     print(script[2*n-2])
#     print(np.linalg.det(rll))
#     print(np.linalg.det(rl))
#     print(np.linalg.det(rll)/np.linalg.det(rl))
#     print(np.linalg.eigvals(rll))
#     print("--------------")

for n,script in data.items():
    print(n)
    for k in range(1,n-2):
        print(k)
        print(n * script[2*k])
        print(script[2*k+1] + (n-1-k)*script[2*k+2] + (k) * script[2*k-2])
        print("-----------")
    print("===============")


# def binomial(n, k):
#     if k == 0:
#         return 1
#     return math.comb(n, k)

# for n,script in data.items():
#     print(n)
#     for k in range(1,n-2):
#         print(binomial(n-2,k-1))
#         print(k/(n-k-1) * binomial(n-2,k))
#         print("-----------")
#     print("===============")
        