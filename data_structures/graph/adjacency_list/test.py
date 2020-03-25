import unittest

from .adjacency_list import AdjacencyListGraph, Vertex


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

    def test_print_graph(self) -> None:
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

    def test_dfs(self) -> None:
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

    def test_bfs(self) -> None:
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

    def test_topological_sort(self) -> None:
        self.assertEqual(
            [v.value for v in self.graph.topological_sort()],
            ["A", "C", "F", "B", "D", "E", "G"],
        )
