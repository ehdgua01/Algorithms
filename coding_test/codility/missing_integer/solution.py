from typing import List


def solution(A: List[int]) -> int:
    A.sort()
    result = 0

    for i in A:
        if 0 < i and 1 < i - result:
            break
        elif 0 < i:
            result = i
    return result + 1
