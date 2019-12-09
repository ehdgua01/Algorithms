"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42584
"""


def solution(prices: list):
    answer = []

    for idx, price in enumerate(prices, start=1):
        count = 0
        for p in prices[idx:]:
            count += 1
            if p < price:
                break
        answer.append(count)
    return answer
