"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque


def solution(bridge_length, weight, truck_weights: list):
    truck_weights = deque(truck_weights)
    on_bridge = []
    answer = 0

    while truck_weights:
        if (
                (len(on_bridge) < bridge_length)
                and (sum(on_bridge) + truck_weights[0]) < weight
        ):
            truck_weight = truck_weights.popleft()
            on_bridge.append(truck_weight)
        answer += 1
    return answer
