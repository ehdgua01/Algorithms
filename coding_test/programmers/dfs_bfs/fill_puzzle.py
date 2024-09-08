import itertools
from collections import deque

xy_distances = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def normalize_polygon(polygon):
    x_min = min(x for x, y in polygon)
    x_max = max(x for x, y in polygon)
    y_min = min(y for x, y in polygon)
    y_max = max(y for x, y in polygon)
    width = x_max - x_min + 1
    height = y_max - y_min + 1
    matrix = [[0] * width for _ in range(height)]
    for x, y in polygon:
        matrix[y][x + abs(x_min)] = 1
    return matrix


def compare_polygon(a, b):
    i = 0
    while i < 4:
        if a == b:
            return True
        b = rotate(b)
        i += 1
    return False


def rotate(polygon):
    return [list(coord) for coord in zip(*reversed(polygon))]


def extract_polygon(grid, active_value, queue):
    p = []
    x_offset, y_offset = queue.popleft()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        grid[y_offset + y][x_offset + x] = 2
        for dx, dy in xy_distances:
            nx, ny = x + dx, y + dy
            gx, gy = x_offset + nx, y_offset + ny
            if 0 > gx or gx >= len(grid) or 0 > gy or gy >= len(grid):
                continue
            if grid[gy][gx] == active_value:
                queue.append((nx, ny))
        p.append((x, y))
    return normalize_polygon(p)


def solution(game_board, table):
    answer, n = 0, len(game_board)
    polygon_on_gb, polygon_on_t = [], []
    q = deque()
    for y in range(n):
        for x in range(n):
            if game_board[y][x] == 0:
                q.append((x, y))
                polygon_on_gb.append(extract_polygon(game_board, 0, q))
            if table[y][x] == 1:
                q.append((x, y))
                polygon_on_t.append(extract_polygon(table, 1, q))
    while polygon_on_t:
        a = polygon_on_t.pop()
        for idx, b in enumerate(polygon_on_gb):
            if b is not None and compare_polygon(a, b):
                polygon_on_gb[idx] = None
                answer += sum(itertools.chain.from_iterable(a))
                break
    return answer


def test_cases():
    assert (
        solution(
            [
                [1, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0],
            ],
            [
                [1, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 0, 0],
                [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0],
            ],
        )
        == 14
    )
    assert (
        solution(
            [
                [0, 0, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )
        == 4
    )
    assert (
        solution(
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 0, 1],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
            ],
        )
        == 5
    )
    assert (
        solution(
            [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 1],
            ],
            [
                [1, 1, 1],
                [1, 0, 0],
                [0, 0, 0],
            ],
        )
        == 0
    )
