"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42747
"""


def solution(citations) -> int:
    citations.sort(reverse=True)
    return next((i for i, c in enumerate(citations) if c <= i), len(citations))
