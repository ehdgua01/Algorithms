"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/43162
"""
from typing import List


def solution(n: int, computers: List[List[int]]) -> int:
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue

        networks = [computers[i]]
        answer += 1
        while networks:
            network = networks.pop()
            for j, connected in enumerate(network):
                if connected and not visited[j]:
                    networks.append(computers[j])
                    visited[j] = True
    return answer
