"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42747
"""

from typing import List


def solution(citations: List[int]) -> int:
    answer = len(citations)
    citations.sort(reverse=True)

    for i, c in enumerate(citations):
        if c <= i:
            answer = i
            break
    return answer
