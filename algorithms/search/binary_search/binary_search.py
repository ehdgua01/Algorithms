"""
파이썬의 기본 라이브러리인 "bisect"로 구현한 코드
https://github.com/TheAlgorithms/Python/blob/master/searches/binary_search.py
"""


def binary_search(data: list, size: int, target):
    if data != sorted(data):
        raise Exception

    left = 0
    right = size - 1

    while left <= right:
        pivot = round((left + right) / 2)
        if data[pivot] == target:
            return data[pivot]
        elif data[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1
