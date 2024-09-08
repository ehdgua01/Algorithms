from collections import deque

arrows = [0, 1, 2, 3]  # 상,하,좌,우
rotate_arrows = [3, 2, 0, 1]
xy_distances = {
    0: [0, -1, "0100"],
    1: [0, 1, "1000"],
    2: [-1, 0, "0001"],
    3: [1, 0, "0010"],
}


def sort_cells(cells):
    return sorted(cells, key=lambda x: tuple(x[a] for a in arrows))


def compare_polygon(a, b):
    b_cells = sort_cells(b)
    if sort_cells(a) == b_cells:
        return True
    for _ in range(3):
        rotate(a)
        if sort_cells(a) == b_cells:
            return True
    return False


def rotate(cells):
    for i, cell in enumerate(cells):
        cells[i] = "".join(cell[from_] for from_ in rotate_arrows)


def extract_polygon(grid, active_value, queue, visited):
    p = []
    while queue:
        x, y, cell = queue.popleft()
        for arrow, (dx, dy, n_cell) in xy_distances.items():
            nx, ny = x + dx, y + dy
            if (0 > nx or nx >= len(grid) or 0 > ny or ny >= len(grid)) or cell[
                arrow
            ] == "1":
                continue
            if grid[ny][nx] == active_value:
                cell = "".join("1" if i == arrow else c for i, c in enumerate(cell))
                if (nx, ny) not in visited:
                    queue.append((nx, ny, n_cell))
                visited.add((nx, ny))
        p.append(cell)
    for x, y in visited:
        grid[y][x] = 2
    return p


def solution(game_board, table):
    answer, n = 0, len(game_board)
    polygons_on_gb, polygons_on_t = [], []
    q = deque()
    for y in range(n):
        for x in range(n):
            if game_board[y][x] == 0:
                q.append((x, y, "0000"))
                polygons_on_gb.append(extract_polygon(game_board, 0, q, {(x, y)}))
            if table[y][x] == 1:
                q.append((x, y, "0000"))
                polygons_on_t.append(extract_polygon(table, 1, q, {(x, y)}))
    while polygons_on_t:
        pt = polygons_on_t.pop()
        for idx, pg in enumerate(polygons_on_gb):
            if pg is not None and compare_polygon(pt, pg):
                polygons_on_gb[idx] = None
                answer += len(pt)
                break
    return answer
