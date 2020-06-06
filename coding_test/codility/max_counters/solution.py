from typing import List


def solution(N: int, A: List[int]) -> List[int]:
    counters = [0] * N
    max_counter = True
    max_ = 0

    for X in A:
        if X == N + 1:
            if max_counter is False:
                counters = [max_] * N
        else:
            counters[X - 1] += 1
            max_counter = False
            if max_ < counters[X - 1]:
                max_ = counters[X - 1]
    return counters
