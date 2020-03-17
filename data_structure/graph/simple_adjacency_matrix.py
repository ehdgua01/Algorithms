"""
Simple adjacency matrix undirected graph
"""
import unittest
from typing import List, Tuple, Any


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

    def print_graph(self) -> List[List[Tuple]]:
        result = []

        if self.is_empty:
            return result

        for vertex in self.vertices:
            result.append([(vertex.index, target) for target in vertex.edges])
        return result

    def dfs(self) -> None:
        if self.is_empty:
            return

        for __vertex in self.vertices:
            for target in __vertex.edges:
                if self.vertices[target].is_visited:
                    continue
                self.vertices[target].visit()

    @property
    def vertex_count(self) -> int:
        return len(self.vertices)

    @property
    def is_empty(self) -> bool:
        return self.vertices is None


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

        vertex_a.create_edge(vertex_b, 0)
        vertex_a.create_edge(vertex_c, 0)

        vertex_b.create_edge(vertex_d, 0)
        vertex_b.create_edge(vertex_e, 0)

        vertex_c.create_edge(vertex_d, 0)
        vertex_c.create_edge(vertex_f, 0)

        vertex_d.create_edge(vertex_e, 0)
        vertex_d.create_edge(vertex_g, 0)

        vertex_e.create_edge(vertex_g, 0)

        vertex_f.create_edge(vertex_g, 0)

    def test_print_graph(self):
        self.assertEqual(
            self.graph.print_graph(),
            [
                [(0, 1), (0, 2)],
                [(1, 0), (1, 3), (1, 4)],
                [(2, 0), (2, 3), (2, 5)],
                [(3, 1), (3, 2), (3, 4), (3, 6)],
                [(4, 1), (4, 3), (4, 6)],
                [(5, 2), (5, 6)],
                [(6, 3), (6, 4), (6, 5)],
            ],
        )

    def test_dfs(self):
        self.graph.dfs()
        self.assertEqual(all([v.is_visited for v in self.graph.vertices]), True)
