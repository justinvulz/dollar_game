from lib.matrix import *
import numpy as np


class Graph:

    def __init__(self, v: int, directed: bool = False) -> None:
        self.nodenum: int = v
        self.adj: list[list[int]] = [[] for i in range(v)]
        self.directed: bool = directed
        self.__invariant_factors: list[int] = []

    def __init__(self, L: np.ndarray, directed: bool = False) -> None:
        self.nodenum: int = L.shape[0]
        self.adj: list[list[int]] = [[] for i in range(self.nodenum)]
        self.directed: bool = directed
        self.__invariant_factors: list[int] = []
        for i in range(self.nodenum):
            for j in range(self.nodenum):
                k =abs(L[i][j])
                self.adj[i].extend([j]*k)

    def get_invariant_factors(self) -> list[int]:
        if not self.__invariant_factors:
            self.__invariant_factors = invariant_factors(self.laplacianMatrix())
        return self.__invariant_factors

    def addEdge(self, v: int, w: int) -> None:
        self.adj[v].append(w)
        if not self.directed:
            self.adj[w].append(v)

    def addEdges(self, edges: list[tuple[int, int]]) -> None:
        for edge in edges:
            self.adj[edge[0]].append(edge[1])
            if not self.directed:
                self.adj[edge[1]].append(edge[0])

    def adjMatrix(self) -> np.ndarray:
        matrix = np.zeros((self.nodenum, self.nodenum))
        for i in range(self.nodenum):
            for j in self.adj[i]:
                matrix[i][j] += 1
        return matrix

    def laplacianMatrix(self) -> np.ndarray:
        matrix = np.zeros((self.nodenum, self.nodenum), dtype=int)
        for i in range(self.nodenum):
            matrix[i][i] = len(self.adj[i])
            for j in self.adj[i]:
                matrix[i][j] += -1
        return matrix

    
