from typing import List, Any


def shell_sort(collection: List[Any]) -> List[Any]:
    gap = len(collection) // 2

    while 0 < gap:
        for i in range(gap, len(collection)):
            j = i
            while j >= gap and collection[j] < collection[j - gap]:
                collection[j], collection[j - gap] = collection[j - gap], collection[j]
                j -= gap
        gap //= 2
    return collection
