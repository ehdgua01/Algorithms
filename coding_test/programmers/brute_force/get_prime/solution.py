"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42839
"""
from itertools import permutations
from math import sqrt, floor


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif 2 < number and number % 2 == 0:
        return False

    max_div = floor(sqrt(number))
    for i in range(3, 1 + max_div, 2):
        if number % i == 0:
            return False
    return True


def solution(numbers: str) -> int:
    answer = set()

    for i in range(1, len(numbers) + 1):
        for number in permutations(numbers, i):
            number = int("".join(number))
            if is_prime(number):
                answer.add(number)
    return len(answer)
