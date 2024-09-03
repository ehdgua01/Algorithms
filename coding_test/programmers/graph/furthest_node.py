from collections import deque


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.distance = 0
        self.neighbors = []
        self.visited = False


def solution(n, edge):
    graph = [Node(idx) for idx in range(1, n + 1)]
    for a, b in edge:
        graph[a - 1].neighbors.append(graph[b - 1])
        graph[b - 1].neighbors.append(graph[a - 1])
    graph[0].visited = True
    queue = deque([graph[0]])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                neighbor.distance = node.distance + 1
                queue.append(neighbor)
    max_distance = max(n.distance for n in graph)
    return sum(n.distance == max_distance for n in graph)


def test_cases():
    assert solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3
