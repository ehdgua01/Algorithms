"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42584
"""
from collections import deque


def solution(prices: list):
    answer = []
    prices = deque(prices)

    while prices:
        price = prices.popleft()
        count = 0
        for p in prices:
            count += 1
            if price > p:
                break
        answer.append(count)
    answer[-1] = 0
    return answer
