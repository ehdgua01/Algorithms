"""
Simple adjacency matrix undirected graph
"""
import unittest
from typing import List, Deque, DefaultDict, Tuple, Any, Dict, Set
from collections import defaultdict, deque


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

    def prim(self) -> Tuple[Dict[int, int], Dict[int, int]]:
        g = self.edges
        known: Set[int] = {
            0,
        }
        mst: Dict[int] = {0: 0}
        path: Dict[int] = {0: 0}

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


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = AdjacencyMatrixGraph()
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        vertex_c = Vertex("C")
        vertex_d = Vertex("D")
        vertex_e = Vertex("E")
        vertex_f = Vertex("F")
        vertex_g = Vertex("G")

        self.graph.add_vertex(vertex_a)
        self.graph.add_vertex(vertex_b)
        self.graph.add_vertex(vertex_c)
        self.graph.add_vertex(vertex_d)
        self.graph.add_vertex(vertex_e)
        self.graph.add_vertex(vertex_f)
        self.graph.add_vertex(vertex_g)

        vertex_a.create_edge(vertex_b, 35)
        vertex_a.create_edge(vertex_c, 100)

        vertex_b.create_edge(vertex_d, 199)
        vertex_b.create_edge(vertex_e, 22)

        vertex_c.create_edge(vertex_d, 33)
        vertex_c.create_edge(vertex_f, 248)

        vertex_d.create_edge(vertex_e, 82)
        vertex_d.create_edge(vertex_g, 104)

        vertex_e.create_edge(vertex_g, 82)

        vertex_f.create_edge(vertex_g, 123)

    def test_print_graph(self) -> None:
        self.assertEqual(
            self.graph.print_graph(),
            {
                "A": {"visited": False, "edges": [(0, 1), (0, 2)]},
                "B": {"visited": False, "edges": [(1, 0), (1, 3), (1, 4)]},
                "C": {"visited": False, "edges": [(2, 0), (2, 3), (2, 5)]},
                "D": {"visited": False, "edges": [(3, 1), (3, 2), (3, 4), (3, 6)]},
                "E": {"visited": False, "edges": [(4, 1), (4, 3), (4, 6)]},
                "F": {"visited": False, "edges": [(5, 2), (5, 6)]},
                "G": {"visited": False, "edges": [(6, 3), (6, 4), (6, 5)]},
            },
        )

    def test_dfs(self) -> None:
        self.graph.dfs()
        self.assertEqual(
            self.graph.print_graph(),
            {
                "A": {"visited": True, "edges": [(0, 1), (0, 2)]},
                "B": {"visited": True, "edges": [(1, 0), (1, 3), (1, 4)]},
                "C": {"visited": True, "edges": [(2, 0), (2, 3), (2, 5)]},
                "D": {"visited": True, "edges": [(3, 1), (3, 2), (3, 4), (3, 6)]},
                "E": {"visited": True, "edges": [(4, 1), (4, 3), (4, 6)]},
                "F": {"visited": True, "edges": [(5, 2), (5, 6)]},
                "G": {"visited": True, "edges": [(6, 3), (6, 4), (6, 5)]},
            },
        )

    def test_bfs(self) -> None:
        self.graph.bfs()
        self.assertEqual(
            self.graph.print_graph(),
            {
                "A": {"visited": True, "edges": [(0, 1), (0, 2)]},
                "B": {"visited": True, "edges": [(1, 0), (1, 3), (1, 4)]},
                "C": {"visited": True, "edges": [(2, 0), (2, 3), (2, 5)]},
                "D": {"visited": True, "edges": [(3, 1), (3, 2), (3, 4), (3, 6)]},
                "E": {"visited": True, "edges": [(4, 1), (4, 3), (4, 6)]},
                "F": {"visited": True, "edges": [(5, 2), (5, 6)]},
                "G": {"visited": True, "edges": [(6, 3), (6, 4), (6, 5)]},
            },
        )

    def test_prim(self) -> None:
        mst, path = self.graph.prim()
        self.assertEqual(path, {0: 0, 1: 0, 4: 1, 6: 4, 5: 6, 2: 3, 3: 4})
        self.assertEqual(sum(mst.values()), 377)
