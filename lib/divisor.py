from lib.graph import Graph


class Divisor:

    def __init__(self, g: Graph, _d: list[int]) -> None:
        self.graph: Graph = g
        self.D: list[int] = _d

    def adj(self, i: int) -> dict:
        return self.graph.adj[i]

    def degree(self) -> int:
        return sum(self.D)

    def firing(self, i: int) -> None:
        for j,m in self.adj(i).items():
            self.D[j] += m
            self.D[i] -= m

    def borring(self, i: int) -> None:
        for j,m in self.adj(i).items():
            self.D[j] -= m
            self.D[i] += m

    def __gt__(self, other) -> bool:
        if isinstance(other, Divisor):
            return self.degree() > other.degree()

        if isinstance(other, int):
            return all(d > other for d in self.D)

    def __ge__(self, other) -> bool:
        # if isinstance(other, Divisor):
            # return self.degree() >= other.degree()

        # if isinstance(other, int):
            return all(d >= other for d in self.D)

    def __lt__(self, other) -> bool:
        if isinstance(other, Divisor):
            return self.degree() < other.degree()

        if isinstance(other, int):
            return all(d < other for d in self.D)

    def __le__(self, other) -> bool:
        if isinstance(other, Divisor):
            return self.degree() <= other.degree()

        if isinstance(other, int):
            return all(d <= other for d in self.D)

    def __getitem__(self, i: int) -> int:
        return self.D[i]


class Config(Divisor):

    def __init__(self, g: Graph, _c: list[int], _rep: int) -> None:
        self.rep: int = _rep
        _c.insert(0, _rep)
        super().__init__(g, _c)

    def firing(self, i: int) -> None:
        super().firing(i)
        self.D[self.rep] = 0

    def borring(self, i: int) -> None:
        super().borring(i)
        self.D[self.rep] = 0
