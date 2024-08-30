"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42583
"""

from collections import deque
from typing import Deque


def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    answer = 0
    elapsed = 0
    weights: Deque = deque(truck_weights)
    on_bridge = deque()
    entered = deque()

    while weights or entered:
        elapsed += 1

        if entered and (elapsed - entered[0] == bridge_length):
            answer = bridge_length + entered.popleft()
            on_bridge.popleft()

        if weights and ((sum(on_bridge) + weights[0]) <= weight):
            on_bridge.append(weights.popleft())
            entered.append(elapsed)
    return answer
