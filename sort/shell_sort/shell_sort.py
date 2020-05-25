from typing import List, Any


def shell_sort(collection: List[Any]) -> List[Any]:
    gap = len(collection) // 2

    while 0 < gap:
        for i in range(gap, len(collection)):
            j, temp = i, collection[i]

            while j >= gap and temp < collection[j - gap]:
                collection[j] = collection[j - gap]
                j -= gap

            collection[j] = temp
        gap //= 2
    return collection
