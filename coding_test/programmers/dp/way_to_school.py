def solution(m, n, puddles):
    grid = [[1] * m for _ in range(n)]
    for x, y in puddles:
        grid[y - 1][x - 1] = 0
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 0:
                continue
            if x == 0:
                grid[y][x] = grid[y - 1][x]
            elif y == 0:
                grid[y][x] = grid[y][x - 1]
            else:
                grid[y][x] = (grid[y][x - 1] + grid[y - 1][x]) % 1_000_000_007
    return grid[n - 1][m - 1]


def test_cases():
    assert solution(1, 3, [[1, 2]]) == 0
    assert solution(4, 3, [[2, 2]]) == 4
