from typing import List, Union, Tuple

RESULT_TYPE = List[List[Tuple[int, int]]]
TABLE_TYPE = List[Union[int, None]]


def is_safe(table: TABLE_TYPE, row: int) -> bool:
    current_row = 0

    while current_row < row:
        if table[current_row] == table[row] or (
            abs(table[current_row] - table[row]) == abs(current_row - row)
        ):
            return False
        current_row += 1
    return True


def find_queen(row: int, table: TABLE_TYPE, result: RESULT_TYPE) -> None:
    if not is_safe(table, row):
        return

    if row == len(table) - 1:
        result.append([(x, y) for y, x in enumerate(table) if x is not None])
    else:
        for i in range(len(table)):
            table[row + 1] = i
            find_queen(row + 1, table, result)


def n_queens(rows: int) -> RESULT_TYPE:
    result: RESULT_TYPE = []
    table: TABLE_TYPE = [None] * rows

    for i in range(rows):
        table[0] = i
        find_queen(0, table, result)

    return result
