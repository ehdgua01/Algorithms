import unittest
from typing import Set, Dict, Tuple

from .adjacency_matrix import Vertex as UndirectedVertex, AdjacencyMatrixGraph


class DirectedVertex(UndirectedVertex):
    def create_edge(self, target, weight: int) -> None:
        self.adjacency_matrix[target.index] = True
        self.weights[target.index] = weight

    def remove_edge(self, target) -> None:
        self.adjacency_matrix[target.index] = False
        self.weights[target.index] = 0


class Prim(AdjacencyMatrixGraph):
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


class TestCase(unittest.TestCase):
    def test_prim(self) -> None:
        graph = Prim()
        vertex_a = DirectedVertex("A")
        vertex_b = DirectedVertex("B")
        vertex_c = DirectedVertex("C")
        vertex_d = DirectedVertex("D")
        vertex_e = DirectedVertex("E")
        vertex_f = DirectedVertex("F")
        vertex_g = DirectedVertex("G")

        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_vertex(vertex_c)
        graph.add_vertex(vertex_d)
        graph.add_vertex(vertex_e)
        graph.add_vertex(vertex_f)
        graph.add_vertex(vertex_g)

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

        self.assertEqual(
            graph.prim(),
            (
                {0: 0, 1: 35, 4: 22, 6: 82, 2: 100, 3: 33, 5: 248},
                {0: 0, 1: 0, 4: 1, 6: 4, 2: 0, 3: 2, 5: 2,},
            ),
        )
