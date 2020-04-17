"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/43164
"""
from typing import List


def dfs(
    tickets: List[List[str]],
    current: str,
    answer: List[str],
    visit: int,
    visited: List[bool],
) -> bool:
    answer.append(current)

    if visit == len(tickets):
        return True

    for i, ticket in enumerate(tickets):
        if ticket[0] == current and visited[i] is False:
            visited[i] = True

            if dfs(tickets, ticket[1], answer, visit + 1, visited):
                return True

            visited[i] = False
    answer.pop()
    return False


def solution(tickets: List[List[str]]) -> List[str]:
    answer = []
    visited = [False] * len(tickets)
    tickets.sort(key=lambda x: x[1])
    dfs(tickets, "ICN", answer, 0, visited)
    return answer
