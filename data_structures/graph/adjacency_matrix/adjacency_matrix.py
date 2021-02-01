"""
Simple adjacency matrix undirected graph
"""
from collections import defaultdict, deque
from functools import reduce
from operator import iconcat
from typing import Any, DefaultDict, Deque, Dict, List, Set, Tuple


class Vertex(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.index: int = -1
        self.visited: bool = False
        self.adjacency_matrix: List[bool] = [False]
        self.weights: List[int] = [0]

    def create_edge(self, target, weight: int) -> None:
        self.adjacency_matrix[target.index] = True
        self.weights[target.index] = weight
        target.adjacency_matrix[self.index] = True
        target.weights[self.index] = weight

    def remove_edge(self, target) -> None:
        self.adjacency_matrix[target.index] = False
        self.weights[target.index] = 0
        target.adjacency_matrx[self.index] = False
        target.weights[self.index] = 0

    def visit(self) -> None:
        self.visited = True

    @property
    def is_visited(self) -> bool:
        return self.visited

    @property
    def edges(self) -> List[int]:
        return [i for i, c in enumerate(self.adjacency_matrix) if c]


class AdjacencyMatrixGraph(object):
    def __init__(self):
        self.vertices: List[Vertex] = []

    def add_vertex(self, __vertex: Vertex) -> None:
        __vertex.index = self.vertex_count
        self.vertices.append(__vertex)

        for __vertex in self.vertices:
            while len(__vertex.adjacency_matrix) - self.vertex_count:
                __vertex.adjacency_matrix.append(False)
                __vertex.weights.append(0)

    def print_graph(self) -> dict:
        result = defaultdict(dict)

        if self.is_empty:
            return result

        for __vertex in self.vertices:
            result[__vertex.value]["visited"] = __vertex.is_visited
            result[__vertex.value]["edges"] = [
                (__vertex.index, target) for target in __vertex.edges
            ]
        return result

    def dfs(self, __vertex: Vertex = None) -> None:
        if self.is_empty:
            return

        __vertex = __vertex if __vertex else self.vertices[0]
        __vertex.visit()

        for target in __vertex.edges:
            if not self.vertices[target].is_visited:
                self.dfs(self.vertices[target])

    def bfs(self) -> None:
        if self.is_empty:
            return

        bfs_queue: Deque[Vertex] = deque([self.vertices[0]])
        while bfs_queue:
            __vertex = bfs_queue.pop()
            __vertex.visit()

            for target in __vertex.edges:
                if not self.vertices[target].is_visited:
                    bfs_queue.appendleft(self.vertices[target])

    def prim(self, start: int = None) -> Tuple[Dict[int, int], Dict[int, int]]:
        g = self.edges
        known: Set[int] = {
            start or 0,
        }
        mst: Dict[int] = {start or 0: 0}
        path: Dict[int] = {start or 0: 0}

        while True:
            if len(g.keys()) == len(mst.keys()):
                break

            min_ = None
            p, c = None, None

            for i in mst:
                for v in g[i]:
                    if v[0] not in known and ((min_ is None) or v[1] < min_):
                        min_ = v[1]
                        p = i
                        c = v

            known.add(c[0])
            mst[c[0]] = c[1]
            path[c[0]] = p
        return mst, path

    def kruskal(self) -> Tuple[Dict[int, int], Dict[int, int]]:
        g = self.edges
        e: List[Tuple] = sorted(
            reduce(iconcat, [[(k, v[0], v[1]) for v in g[k]] for k in g.keys()], []),
            key=lambda v: v[2],
            reverse=True,
        )
        mst = {}
        path = {}
        s = [{i} for i in g.keys()]

        while True:
            if len(s) == 1:
                break

            x = e.pop()
            from_, to = None, None

            for index, v in enumerate(s):
                if x[0] in v:
                    from_ = index

                if x[1] in v:
                    to = index

            if from_ != to:
                s[from_].update(s[to])
                s.pop(to)
                mst[x[1]] = x[2]
                path[x[1]] = x[0]
        return mst, path

    def dijkstra(self, start: int = None):
        g = self.edges
        mst: Dict[int] = {start or 0: 0}
        path: Dict[int] = {start or 0: 0}
        known: Set[int] = set()

        while True:
            if len(known) == len(g.keys()):
                break

            for i in set(mst.keys()) - known:
                for v in g[i]:
                    weight = mst.get(v[0], None)
                    if (weight is None) or ((mst[i] + v[1]) < weight):
                        mst[v[0]] = mst[i] + v[1]
                        path[v[0]] = i
                known.add(i)
        return mst, path

    @property
    def vertex_count(self) -> int:
        return len(self.vertices)

    @property
    def is_empty(self) -> bool:
        return self.vertices is None

    @property
    def edges(self) -> DefaultDict[int, List[Tuple[int]]]:
        """
        return all edges (target node index, weight)
        :return: {
            "0": [[1, 32]]  # [[node index, weight]]
        }
        """
        g = defaultdict(list)

        for v in self.vertices:
            for i in v.edges:
                g[v.index].append((i, v.weights[i]))
        return g
