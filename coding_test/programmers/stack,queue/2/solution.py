"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42587
"""


def solution(priorities, location):
    priorities[location] = float(priorities[location])
    count = 0

    while True:
        if priorities[0] != max(priorities):
            priorities.append(priorities.pop(0))
        else:
            answer = priorities.pop(0)
            count += 1

            if isinstance(answer, float):
                return count
