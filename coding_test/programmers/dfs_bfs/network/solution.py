"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/43162
"""
from typing import List


def solution(n: int, computers: List[List[int]]) -> int:
    answer = 0
    known = set()

    for i in range(n):
        if i in known:
            continue

        network = [computers[i]]
        answer += 1
        known.add(i)

        while network:
            computer = network.pop()

            for index, c in enumerate(computer):
                if c == 1 and index not in known:
                    known.add(index)
                    network.append(computers[index])
    return answer
