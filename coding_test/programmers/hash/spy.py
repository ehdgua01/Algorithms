"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42578
"""


from collections import Counter
from functools import reduce


def solution(clothes):
    clothes_types = Counter([value[1] for value in clothes])
    answer = reduce(lambda x, y: x * (y + 1), clothes_types.values(), 1)
    return answer - 1
