from typing import List


def solution(A: List[int]) -> int:
    if len(A) == 0:
        return 1

    A = set(A)
    return list(set(range(1, len(A) + 2)).difference(A))[0]
