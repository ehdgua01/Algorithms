from typing import List, Tuple, Union

RESULT_TYPE = List[List[Tuple[int, int]]]
BOARD_TYPE = List[Union[int, None]]


def is_safe(board: BOARD_TYPE, row: int) -> bool:
    current_row = 0

    while current_row < row:
        if board[current_row] == board[row] or (
            abs(board[current_row] - board[row]) == abs(current_row - row)
        ):
            return False
        current_row += 1
    return True


def find_queen(row: int, board: BOARD_TYPE, result: RESULT_TYPE) -> None:
    if not is_safe(board, row):
        return

    if row == len(board) - 1:
        result.append([(x, y) for y, x in enumerate(board) if x is not None])
    else:
        for i in range(len(board)):
            board[row + 1] = i
            find_queen(row + 1, board, result)


def n_queens(rows: int) -> RESULT_TYPE:
    result: RESULT_TYPE = []
    board: BOARD_TYPE = [None] * rows

    for i in range(rows):
        board[0] = i
        find_queen(0, board, result)

    return result
