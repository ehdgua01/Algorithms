"""
Simple adjacency list directed graph
"""
import unittest
from typing import Union, Any, Deque
from collections import deque


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
        self.bfs_queue: Deque[Vertex] = deque()

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

    def dfs(self, vertex: Vertex = None) -> None:
        if self.is_empty:
            return

        __vertex = vertex if vertex else self.vertices
        __vertex.visited = True
        __edge = __vertex.adjacency_list

        while __edge is not None:
            if not __edge.target.visited:
                self.dfs(__edge.target)
            __edge = __edge.next

    def bfs(self) -> None:
        if self.is_empty:
            return

        self.vertices.visited = True
        self.bfs_queue.append(self.vertices)
        while self.bfs_queue:
            __vertex = self.bfs_queue.pop()
            __edge = __vertex.adjacency_list

            while __edge is not None:
                if not __edge.target.visited:
                    __edge.target.visited = True
                    self.bfs_queue.appendleft(__edge.target)
                __edge = __edge.next

    @property
    def is_empty(self) -> bool:
        return self.vertices is None


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = AdjacencyListGraph()
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

        vertex_a.create_edge(vertex_b)
        vertex_a.create_edge(vertex_c)

        vertex_b.create_edge(vertex_d)
        vertex_b.create_edge(vertex_e)

        vertex_c.create_edge(vertex_d)
        vertex_c.create_edge(vertex_f)

        vertex_d.create_edge(vertex_e)
        vertex_d.create_edge(vertex_g)

        vertex_e.create_edge(vertex_g)

        vertex_f.create_edge(vertex_g)

    def test_print_graph(self):
        self.assertEqual(
            self.graph.print_graph(),
            {
                "A": {"adjacency_list": {"B": 0, "C": 0}, "visited": False},
                "B": {"adjacency_list": {"D": 0, "E": 0}, "visited": False},
                "C": {"adjacency_list": {"D": 0, "F": 0}, "visited": False},
                "D": {"adjacency_list": {"E": 0, "G": 0}, "visited": False},
                "E": {"adjacency_list": {"G": 0}, "visited": False},
                "F": {"adjacency_list": {"G": 0}, "visited": False},
                "G": {"adjacency_list": {}, "visited": False},
            },
        )

    def test_dfs(self):
        self.graph.dfs()
        self.assertEqual(
            self.graph.print_graph(),
            {
                "A": {"adjacency_list": {"B": 0, "C": 0}, "visited": True},
                "B": {"adjacency_list": {"D": 0, "E": 0}, "visited": True},
                "C": {"adjacency_list": {"D": 0, "F": 0}, "visited": True},
                "D": {"adjacency_list": {"E": 0, "G": 0}, "visited": True},
                "E": {"adjacency_list": {"G": 0}, "visited": True},
                "F": {"adjacency_list": {"G": 0}, "visited": True},
                "G": {"adjacency_list": {}, "visited": True},
            },
        )

    def test_bfs(self):
        self.graph.bfs()
        self.assertEqual(
            self.graph.print_graph(),
            {
                "A": {"adjacency_list": {"B": 0, "C": 0}, "visited": True},
                "B": {"adjacency_list": {"D": 0, "E": 0}, "visited": True},
                "C": {"adjacency_list": {"D": 0, "F": 0}, "visited": True},
                "D": {"adjacency_list": {"E": 0, "G": 0}, "visited": True},
                "E": {"adjacency_list": {"G": 0}, "visited": True},
                "F": {"adjacency_list": {"G": 0}, "visited": True},
                "G": {"adjacency_list": {}, "visited": True},
            },
        )
