"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42585
"""


def solution(arrangement: str) -> int:
    answer = 0
    pipes = 0
    is_laser = False

    for a in arrangement:
        if a == ")":
            if is_laser:
                answer += pipes - 1
                is_laser = False
            else:
                answer += 1
            pipes -= 1
        else:
            pipes += 1
            is_laser = True
    return answer
