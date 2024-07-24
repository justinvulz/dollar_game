from lib.matrix import *
import numpy as np


class Graph:

    def __init__(self, v: int, directed: bool = False) -> None:
        self.nodenum: int = v
        self.adj: list[dict] = [dict() for _ in range(v)]
        self.directed: bool = directed
        self.__invariant_factors: list[int] = []

    def get_invariant_factors(self) -> list[int]:
        if not self.__invariant_factors:
            self.__invariant_factors = invariant_factors(
                self.laplacianMatrix())
        return self.__invariant_factors

    def addEdge(self, v: int, w: int, m:int =1) -> None:
        self.adj[v][w] = self.adj[v].get(w, 0)+m
        if not self.directed:
            self.adj[w][v] = self.adj[w].get(v, 0)+m

    def addEdges(self, edges: list[tuple[int, int]]) -> None:
        for v, w in edges:
            self.addEdge(v, w)
        if not self.directed:
            for w, v in edges:
                self.addEdge(v, w)

    def adjMatrix(self) -> np.ndarray:
        matrix = np.zeros((self.nodenum, self.nodenum))
        for i in range(self.nodenum):
            for j, m in self.adj[i].items():
                matrix[i][j] += m
        return matrix

    def laplacianMatrix(self) -> np.ndarray:
        matrix = np.zeros((self.nodenum, self.nodenum), dtype=int)
        for i in range(self.nodenum):
            matrix[i][i] = sum(m for m in self.adj[i].values())
            for j, m in self.adj[i].items():
                matrix[i][j] += -m
        return matrix
