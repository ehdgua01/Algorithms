import unittest
from typing import Union, Any


class Edge(object):
    def __init__(self, from_, target, weight: int) -> None:
        self.weight = weight
        self.next: Union[Edge, None] = None
        self.from_: Vertex = from_
        self.target: Vertex = target


class Vertex(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.visited: bool = False
        self.index: int = -1
        self.next: Union[Vertex, None] = None
        self.adjacency_list: Union[Edge, None] = None

    def create_edge(self, target) -> None:
        __edge = Edge(self, target, 0)

        if self.adjacency_list is None:
            self.adjacency_list = __edge
        else:
            adjacency_list = self.adjacency_list
            while adjacency_list.next is not None:
                adjacency_list = adjacency_list.next
            adjacency_list.next = __edge


class AdjacencyListGraph(object):
    def __init__(self) -> None:
        self.vertices: Union[Vertex, None] = None
        self.vertex_count: int = 0

    def add_vertex(self, vertex: Vertex) -> None:
        if self.is_empty:
            self.vertices = vertex
        else:
            current_vertex = self.vertices
            while current_vertex.next is not None:
                current_vertex = current_vertex.next
            current_vertex.next = vertex
        vertex.index = self.vertex_count = self.vertex_count + 1

    def print_graph(self) -> dict:
        result = {}

        if self.is_empty:
            return result

        current_vertex = self.vertices
        while current_vertex is not None:
            result[current_vertex.value] = {
                "adjacency_list": {},
                "visited": current_vertex.visited,
            }

            if current_vertex.adjacency_list is not None:
                __edge = current_vertex.adjacency_list
                while __edge is not None:
                    result[current_vertex.value]["adjacency_list"][
                        __edge.target.value
                    ] = __edge.weight
                    __edge = __edge.next

            current_vertex = current_vertex.next
        return result

    @property
    def is_empty(self) -> bool:
        return self.vertices is None


class TestCase(unittest.TestCase):
    def test_graph(self):
        graph = AdjacencyListGraph()
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        vertex_c = Vertex("C")
        vertex_d = Vertex("D")
        vertex_e = Vertex("E")

        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_vertex(vertex_c)
        graph.add_vertex(vertex_d)
        graph.add_vertex(vertex_e)

        vertex_a.create_edge(vertex_b)
        vertex_a.create_edge(vertex_c)
        vertex_a.create_edge(vertex_d)
        vertex_a.create_edge(vertex_e)

        vertex_b.create_edge(vertex_a)
        vertex_b.create_edge(vertex_c)
        vertex_b.create_edge(vertex_e)

        vertex_c.create_edge(vertex_a)
        vertex_c.create_edge(vertex_b)

        vertex_d.create_edge(vertex_a)
        vertex_d.create_edge(vertex_e)

        vertex_e.create_edge(vertex_a)
        vertex_e.create_edge(vertex_b)
        vertex_e.create_edge(vertex_d)

        self.assertEqual(
            graph.print_graph(),
            {
                "A": {
                    "adjacency_list": {"B": 0, "C": 0, "D": 0, "E": 0},
                    "visited": False,
                },
                "B": {"adjacency_list": {"A": 0, "C": 0, "E": 0}, "visited": False},
                "C": {"adjacency_list": {"A": 0, "B": 0}, "visited": False},
                "D": {"adjacency_list": {"A": 0, "E": 0}, "visited": False},
                "E": {"adjacency_list": {"A": 0, "B": 0, "D": 0}, "visited": False},
            },
        )
