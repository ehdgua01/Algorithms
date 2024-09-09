from collections import defaultdict, deque


def solution(n, wires):
    answer = n
    graph = defaultdict(set)
    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)
    queue = deque()
    for unconnected in wires:
        queue.append(wires[0][0])
        connected = set()
        while queue:
            a = queue.popleft()
            connected.add(a)
            for b in graph[a]:
                if (a in unconnected and b in unconnected) or b in connected:
                    continue
                connected.add(b)
                queue.append(b)
        answer = min(answer, abs(n - len(connected) * 2))
    return answer


def test_cases():
    assert (
        solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
        == 3
    )
    assert solution(4, [[1, 2], [2, 3], [3, 4]]) == 0
    assert solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]) == 1
