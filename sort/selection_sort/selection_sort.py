from typing import List


def selection_sort(data: List[int]) -> List[int]:
    for i in range(len(data) - 1):
        least = i

        for j in range(i + 1, len(data)):
            if data[j] < data[least]:
                least = j

        if i != least:
            data[i], data[least] = data[least], data[i]
    return data
