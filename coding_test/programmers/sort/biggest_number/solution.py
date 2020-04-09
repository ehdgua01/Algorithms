"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42746
"""
from typing import List, Tuple


def solution(numbers: List[int]) -> str:
    answer: List[Tuple[str, str]] = []

    for n in numbers:
        string_n = str(n)
        answer.append((string_n, (string_n * 3)[0:4]))

    answer.sort(key=lambda x: x[1], reverse=True)
    return str(int("".join(map(lambda x: x[0], answer))))
