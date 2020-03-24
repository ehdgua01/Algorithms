from typing import List, Tuple, Union

TYPES = {
    " ": 0,
    "#": 1,
    "M": 2,
    "S": 3,
    "G": 4,
}
MAZE = List[List[int]]
POSITION = Tuple[int, int]


def parse_maze(maze: str) -> Tuple[MAZE, POSITION]:
    start_pos = None
    maze_info = []

    for y, line in enumerate(maze.splitlines()):
        maze_info.append([])

        for x, pos in enumerate(line):
            maze_info[y].append(TYPES[pos])

            if pos == "S":
                start_pos = (x, y)

    if start_pos is None:
        raise ValueError
    else:
        return maze_info, start_pos


def next_step(
    maze: MAZE, current_pos: POSITION, direction: int
) -> Union[POSITION, bool]:
    x, y = current_pos

    if direction == 0:
        y += 1
        if len(maze) <= y:
            return False
    elif direction == 1:
        x += 1
        if len(maze[y]) <= x:
            return False
    elif direction == 2:
        y -= 1
        if y < 0:
            return False
    elif direction == 3:
        x -= 1
        if x < 0:
            return False

    if maze[y][x] == TYPES["#"]:
        return False
    elif maze[y][x] == TYPES["M"]:
        return False
    return x, y


def search_goal(maze: MAZE, current_pos: POSITION, ways: List[POSITION]) -> bool:
    x, y = current_pos
    ways.append(current_pos)

    if maze[y][x] == TYPES["G"]:
        maze[y][x] = TYPES["M"]
        return True

    maze[y][x] = TYPES["M"]

    for direction in range(4):
        next_pos = next_step(maze, current_pos, direction)

        if not next_pos:
            continue

        if search_goal(maze, next_pos, ways):
            return True

    maze[x][y] = TYPES[" "]
    ways.pop()
    return False


def escape_maze(maze: str) -> Union[List[POSITION], bool]:
    ways: List[POSITION] = []
    maze_info, start_pos = parse_maze(maze)
    result = search_goal(maze_info, start_pos, ways)

    if result:
        return ways
    else:
        return False
