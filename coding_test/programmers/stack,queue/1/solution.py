"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42586
"""
from collections import defaultdict


def solution(progresses, speeds):
    """
    먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
    각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를
    return 하도록 solution 함수를 완성하세요.

    :param progresses: 작업 우선순위로 작업 진도가 정렬, 100 미만
    :param speeds: 작업의 하루 작업 속도, 100 이하
    :return:
    """
    scheduler = defaultdict(int)
    last_deploy = 0

    for p, s in zip(progresses, speeds):
        q, r = divmod(100 - p, s)
        when_deploy = q if r == 0 else q + 1

        if last_deploy <= when_deploy:
            last_deploy = when_deploy

        scheduler[last_deploy] += 1

    return list(scheduler.values())
