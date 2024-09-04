from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    xy_distances = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    distances = [[-1] * m for _ in range(n)]
    distances[0][0] = 1
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return distances[-1][-1]
        for dx, dy in xy_distances:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    return -1


def test_cases():
    assert (
        solution(
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1],
            ]
        )
        == 11
    )
    assert (
        solution(
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1],
            ]
        )
        == -1
    )
    assert (
        solution(
            [
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
            ]
        )
        == 9
    )
    assert (
        solution(
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ]
        )
        == 9
    )
    assert (
        solution(
            [
                [1, 0, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 1],
            ]
        )
        == -1
    )
    assert solution([[1, 1], [1, 1]]) == 3
