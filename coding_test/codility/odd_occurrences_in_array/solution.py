from typing import List
from collections import Counter


def solution(A: List[int]) -> int:
    for k, v in Counter(A).items():
        if v % 2 == 1:
            return k
