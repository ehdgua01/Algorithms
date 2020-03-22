from typing import List


def lcs(x: str, y: str, data: List[List[int]]) -> int:
    i, j = len(x), len(y)

    for m in range(1, i + 1):
        for n in range(1, j + 1):
            if x[m - 1] == y[n - 1]:
                match = 1
            else:
                match = 0
            data[m][n] = max(data[m - 1][n], data[m][n - 1], data[m - 1][n - 1] + match)
    return data[i][j]
