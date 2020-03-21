from typing import List


def simple_lcs(x: str, y: str, i: int, j: int, data: List[List[int]]) -> int:
    if (i == 0) or (j == 0):
        data[i][j] = 0
    elif x[i - 1] == y[j - 1]:
        data[i][j] = simple_lcs(x, y, i - 1, j - 1, data) + 1
    else:
        data[i][j] = max(
            simple_lcs(x, y, i - 1, j, data), simple_lcs(x, y, i, j - 1, data)
        )
    return data[i][j]
