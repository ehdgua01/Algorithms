"""
Simple adjacency list directed graph
"""

from collections import deque
from typing import Any, Deque, Union


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

    def create_edge(self, target, weight) -> None:
        __edge = Edge(self, target, weight)

        if self.adjacency_list is None:
            self.adjacency_list = __edge
        else:
            adjacency_list = self.adjacency_list
            while adjacency_list.next is not None:
                adjacency_list = adjacency_list.next
            adjacency_list.next = __edge

    def visit(self) -> None:
        self.visited = True

    @property
    def is_visited(self) -> bool:
        return self.visited


class AdjacencyListGraph(object):
    def __init__(self) -> None:
        self.vertices: Union[Vertex, None] = None
        self.vertex_count: int = 0

    def add_vertex(self, __vertex: Vertex) -> None:
        if self.is_empty:
            self.vertices = __vertex
        else:
            current_vertex = self.vertices
            while current_vertex.next is not None:
                current_vertex = current_vertex.next
            current_vertex.next = __vertex
        __vertex.index = self.vertex_count = self.vertex_count + 1

    def print_graph(self) -> dict:
        result = {}

        if self.is_empty:
            return result

        current_vertex = self.vertices
        while current_vertex is not None:
            result[current_vertex.value] = {
                "adjacency_list": {},
                "visited": current_vertex.is_visited,
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

    def dfs(self, __vertex: Vertex = None) -> None:
        if self.is_empty:
            return

        __vertex = __vertex if __vertex else self.vertices
        __vertex.visit()
        __edge = __vertex.adjacency_list

        while __edge is not None:
            if not __edge.target.is_visited:
                self.dfs(__edge.target)
            __edge = __edge.next

    def bfs(self) -> None:
        if self.is_empty:
            return

        self.vertices.visit()
        bfs_queue: Deque[Vertex] = deque()
        bfs_queue.append(self.vertices)

        while bfs_queue:
            __vertex = bfs_queue.pop()
            __edge = __vertex.adjacency_list

            while __edge is not None:
                if not __edge.target.is_visited:
                    __edge.target.visit()
                    bfs_queue.appendleft(__edge.target)
                __edge = __edge.next

    def topological_sort(self, __vertex: Vertex = None) -> Union[Deque[Vertex], None]:
        if self.is_empty:
            return

        __vertex = __vertex if __vertex else self.vertices
        __vertex.visit()
        __edge = __vertex.adjacency_list
        result = deque()

        while __edge is not None:
            temp = deque()

            if not __edge.target.is_visited:
                temp.extendleft(self.topological_sort(__edge.target))

            result.extendleft(temp)
            __edge = __edge.next
        result.appendleft(__vertex)
        return result

    @property
    def is_empty(self) -> bool:
        return self.vertices is None
