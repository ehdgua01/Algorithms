"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42628
"""
from typing import List


def solution(operations: List[str]) -> List[int]:
    q = []

    for operation in operations:
        command, val = operation.split()
        val = int(val)

        if command == "I":
            q.append(val)
        elif q:
            if val == -1:
                q.remove(min(q))
            else:
                q.remove(max(q))
    return [max(q), min(q)] if q else [0, 0]
