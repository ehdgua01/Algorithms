"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/43165
"""
from operator import add, sub
from typing import List


def dfs(numbers: List[int], target: int, current: int, result: List[bool]) -> bool:
    if len(numbers) == 0:
        if current == target:
            return True
    else:
        for operator in [add, sub]:
            if dfs(numbers[1:], target, operator(current, numbers[0]), result):
                result.append(True)
    return False


def solution(numbers: List[int], target: int) -> int:
    result = []
    dfs(numbers, target, 0, result)
    return len(result)
