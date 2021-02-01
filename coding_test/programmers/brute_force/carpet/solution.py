"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42842
"""
from math import floor, sqrt
from typing import List


def solution(brown: int, red: int) -> List[int]:
    total = brown + red
    max_div = floor(sqrt(total))

    for height in range(max_div, 0, -1):
        if total % height == 0:
            width = total // height

            if (width - 2) * (height - 2) == red:
                return [width, height]
