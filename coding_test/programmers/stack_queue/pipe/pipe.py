"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42585
"""


def solution(arrangement: str) -> int:
    answer: int = 0
    pipes: int = 0
    is_laser: bool = False

    for a in arrangement:
        if a == ")":
            pipes -= 1
            if is_laser:
                answer += pipes
                is_laser = False
            else:
                answer += 1
        else:
            pipes += 1
            is_laser = True
    return answer
