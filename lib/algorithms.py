from lib.divisor import Divisor, Config
from lib.graph import Graph
import numba


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n*factorial(n-1)


def combination(n: int, k: int) -> int:
    return factorial(n)//(factorial(k)*factorial(n-k))


def greedy(D: Divisor) -> list[int]:
    n = D.graph.nodenum
    S = set()
    ans = [0 for _ in range(n)]
    buffer = [i for i in range(n) if D.D[i] < 0]
    while buffer:
        if not len(S) == n:
            v = buffer[0]
            D.borring(v)
            ans[v] -= 1
            if v not in S:
                S.add(v)
            buffer = [i for i in range(n) if D.D[i] < 0]
        else:
            return []
    return ans

# change the graph implementation, not sure if it will work


def Dhar(c: Config) -> list[int]:
    S = [i for i in range(c.graph.nodenum)]
    S.remove(c.rep)

    def outdegree(i, S):
        count = 0
        for j in c.adj(i):
            if j not in S:
                count += 1
        return count

    while S:
        flag = True
        for i in S:
            if c[i] < outdegree(i, S):
                flag = False
                S.remove(i)
        if flag:
            return S
    return S


# change the graph implementation, not sure if it will work
def get_q_reduced(D: Divisor, q: int) -> Divisor:
    while all(D[i] >= 0 for i in range(D.graph.nodenum) if i != q):
        v = [i for i in range(D.graph.nodenum) if D[i] < 0 and i != q][0]
        D.borring(v)

    #
    c = Config(D.graph, D.D, q)
    S = Dhar(c)
    while S:
        for i in S:
            D.firing(i)
        c = Config(D.graph, D.D, q)
        S = Dhar(c)
    return D
