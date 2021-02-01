"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42841
"""
from itertools import permutations
from typing import List


def solution(baseball: List[List[int]]) -> int:
    answer = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))

    for q in baseball:
        if q[1] == 3:
            return 1

        str_ = str(q[0])

        for a in answer[:]:
            S = 0

            for i in range(3):
                if str_[i] == a[i]:
                    S += 1

            B = len(set(str_).intersection(a)) - S

            if S != q[1] or B != q[2]:
                answer.remove(a)
    return len(answer)
