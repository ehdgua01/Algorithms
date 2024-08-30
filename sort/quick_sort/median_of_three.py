"""
퀵 정렬의 최악의 경우를 피하는 방법
기준 요소를 평균값으로 결정하여 정렬한다.
"""

from typing import Any, List


def median_of_three_quick_sort(data: List[Any], left: int, right: int) -> List[Any]:
    if right <= left:
        return data

    lesser = index = left
    median = data[(left + right) // 2]
    pivot = data[
        data.index(
            (data[left] + data[right] + median)
            - max([data[left], data[right], median])
            - min([data[left], data[right], median])
        )
    ]
    greater = right

    while index <= greater:
        if data[index] < pivot:
            data[lesser], data[index] = data[index], data[lesser]
            lesser += 1
            index += 1
        elif pivot < data[index]:
            data[greater], data[index] = data[index], data[greater]
            greater -= 1
        else:
            index += 1

    median_of_three_quick_sort(data, left, lesser - 1)
    median_of_three_quick_sort(data, greater + 1, right)
    return data
