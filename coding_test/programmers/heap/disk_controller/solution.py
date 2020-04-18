"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42627
"""
from typing import List


def solution(jobs: List[List[int]]) -> int:
    run_time = 0
    current = 0
    count = len(jobs)

    while jobs:
        available_jobs = [x for x in jobs if x[0] <= current]
        if available_jobs:
            job = min(available_jobs, key=lambda x: x[1])
            run_time += (current - job[0]) + job[1]
            current += job[1]
            jobs.remove(job)
        else:
            current += 1
    return run_time // count
