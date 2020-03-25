import unittest

from .adjacency_matrix import AdjacencyMatrixGraph, Vertex


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
        mst, path = self.graph.prim(1)
        self.assertEqual(path, {1: 0, 4: 1, 0: 1, 3: 4, 2: 3, 6: 4, 5: 6})
        self.assertEqual(sum(mst.values()), 377)

    def test_kruskal(self) -> None:
        mst, path = self.graph.kruskal()
        self.assertEqual(path, {0: 1, 1: 4, 2: 3, 3: 4, 4: 6, 5: 6})
        self.assertEqual(sum(mst.values()), 377)

    def test_dijkstra(self) -> None:
        mst, path = self.graph.dijkstra(5)
        self.assertEqual(mst, {5: 0, 2: 248, 6: 123, 4: 205, 3: 227, 1: 227, 0: 262})
        self.assertEqual(path, {5: 0, 2: 5, 6: 5, 4: 6, 3: 6, 1: 4, 0: 1})
