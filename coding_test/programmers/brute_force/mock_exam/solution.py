"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42840
"""

from math import ceil
from typing import List


def solution(answers: List[int]) -> List[int]:
    result = [0, 0, 0]

    for answer, a, b, c in zip(
        answers,
        "12345" * ceil(len(answers) / 5),
        "21232425" * ceil(len(answers) / 8),
        "3311224455" * ceil(len(answers) / 10),
    ):
        answer = str(answer)

        if a == answer:
            result[0] += 1

        if b == answer:
            result[1] += 1

        if c == answer:
            result[2] += 1

    max_ = max(result)
    return [i for i, x in enumerate(result, start=1) if x == max_]
