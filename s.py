import sympy
from sympy import *
from sympy.functions.combinatorial.factorials import binomial

def printlatex(expr):
    lexper = latex(expr)
    lexper = lexper.replace("\\left[", "")
    lexper = lexper.replace("\\right]", "")
    lexper = lexper.replace("matrix", "pmatrix")
    print(lexper+"\\\\")


class Graph:

    def __init__(self, v: int, directed: bool = False) -> None:
        self.nodenum: int = v
        self.adj: list[dict] = [dict() for _ in range(v)]
        self.directed: bool = directed
        self.__invariant_factors: list[int] = []

    def addEdge(self, v: int, w: int, m:int =1) -> None:
        self.adj[v][w] = self.adj[v].get(w, 0)+m
        if not self.directed:
            self.adj[w][v] = self.adj[w].get(v, 0)+m

    def laplacianMatrix(self)  :
        matrix = Matrix(self.nodenum, self.nodenum, lambda i,j: 0)
        for i in range(self.nodenum):
            matrix[i,i] = sum(m for m in self.adj[i].values())
            for j, m in self.adj[i].items():
                matrix[i,j] += -m
        # for i in range(self.nodenum):
        #     for j in range(self.nodenum):
        #         matrix[i,j] = simplify(matrix[i,j])
        return matrix

def ncube_reduce_graph(ni: int) -> Graph:
    nk = ni*2
    n = Symbol('n')
    g = Graph(nk)
    for i in range(ni):
        g.addEdge(2*i, 2*i+1,binomial(n-1, i))

    for i in range(ni-1):
        g.addEdge(2*i, 2*i+2,binomial(n-1, i)*(n-1-i))
        g.addEdge(2*i+1, 2*i+3,binomial(n-1, i)*(n-1-i))
    
    return g

init_printing()
for n in range(2,6):
    g = ncube_reduce_graph(n)
    l = g.laplacianMatrix()

    Matrix.row_del(l, 1)
    Matrix.col_del(l, 1)
    printlatex(l.det())