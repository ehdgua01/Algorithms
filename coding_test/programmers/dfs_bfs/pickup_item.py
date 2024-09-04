from collections import deque

x_distances = [0, 1, 0, -1]
y_distances = [1, 0, -1, 0]


def solution(rectangle, character_x, character_y, item_x, item_y):
    grid = [[0] * 102 for _ in range(102)]
    distances = [[-1] * 102 for _ in range(102)]
    for min_x, min_y, max_x, max_y in rectangle:
        min_x, min_y, max_x, max_y = min_x * 2, min_y * 2, max_x * 2, max_y * 2
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if min_x < x < max_x and min_y < y < max_y:
                    grid[x][y] = 2
                elif grid[x][y] != 2:
                    grid[x][y] = 1

    cx, cy, ix, iy = character_x * 2, character_y * 2, item_x * 2, item_y * 2
    queue = deque([(cx, cy)])
    distances[cx][cy] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(x_distances, y_distances):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > 101 or ny < 0 or ny > 101:
                continue
            if grid[nx][ny] == 1 and distances[nx][ny] == -1:
                queue.append((nx, ny))
                distances[nx][ny] = distances[x][y] + 1
    return distances[ix][iy] // 2


def test_cases():
    assert (
        solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
        == 17
    )
    assert (
        solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
        == 11
    )
    assert solution([[1, 1, 5, 7]], 1, 1, 4, 7) == 9
    assert solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10) == 15
    assert solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3) == 10
    assert (
        solution([[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]], 3, 2, 5, 4)
        == 8
    )
    assert solution([[1, 1, 4, 4], [2, 2, 5, 5], [3, 3, 7, 8]], 1, 1, 5, 3) == 6
    assert solution([[1, 1, 2, 2]], 1, 1, 2, 2) == 2
    assert solution([[1, 1, 50, 5]], 1, 1, 50, 5) == 53
