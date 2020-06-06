from typing import List


def solution(N: int, A: List[int]) -> List[int]:
    counters = [0] * N
    max_ = max_counter = 0

    for X in A:
        if X == N + 1:
            max_counter = max_
        else:
            current = counters[X - 1] = max(counters[X - 1] + 1, max_counter + 1)
            max_ = max(current, max_)
    return [c if c > max_counter else max_counter for c in counters]
