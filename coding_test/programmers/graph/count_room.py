from collections import defaultdict

x_distances = [0, 1, 1, 1, 0, -1, -1, -1]
y_distances = [1, 1, 0, -1, -1, -1, 0, 1]


def move(pos, arrow):
    x, y = pos
    return x + x_distances[arrow], y + y_distances[arrow]


def solution(arrows):
    graph = defaultdict(list)
    pos = 0, 0
    graph[pos] = []
    answer = 0
    for arrow in arrows:
        for _ in range(2):
            next_pos = move(pos, arrow)
            visited = next_pos in graph
            new_edge = pos not in graph[next_pos]
            if visited and new_edge:
                graph[pos].append(next_pos)
                graph[next_pos].append(pos)
                answer += 1
            elif new_edge:
                graph[pos].append(next_pos)
                graph[next_pos].append(pos)
            pos = next_pos
    return answer


def test_cases():
    assert solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]) == 3
    assert solution([1, 4, 7]) == 1
