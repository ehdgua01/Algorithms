"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42588
"""


def solution(heights: list) -> list:
    answer: list = []
    heights.reverse()

    for idx, height in enumerate(heights, start=1):
        receiver = 0

        for i, h in enumerate(heights[idx:]):
            if h > height:
                receiver = len(heights) - i - idx
                break

        answer.insert(0, receiver)
    return answer
