from collections import Counter
from typing import List


def solution(A: List[int]) -> int:
    for k, v in Counter(A).items():
        if v % 2 == 1:
            return k
