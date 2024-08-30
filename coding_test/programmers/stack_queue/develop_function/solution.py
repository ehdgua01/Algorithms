"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42586
"""

from collections import defaultdict


def solution(progresses, speeds):
    scheduler = defaultdict(int)
    last_deploy = 0

    for p, s in zip(progresses, speeds):
        q, r = divmod(100 - p, s)
        when_deploy = q if r == 0 else q + 1

        if last_deploy <= when_deploy:
            last_deploy = when_deploy

        scheduler[last_deploy] += 1

    return list(scheduler.values())
