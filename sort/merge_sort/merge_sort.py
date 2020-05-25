from typing import Union, List, Any


def merge_sort(data: List[Any], left: int, right: int) -> Union[List[Any], None]:
    if (right - left) < 2:
        return

    a = left
    b = middle = (right + left) // 2
    temp = []

    merge_sort(data, left, middle)
    merge_sort(data, middle, right)

    while a < middle and b < right:
        if data[a] <= data[b]:
            temp.append(data[a])
            a += 1
        else:
            temp.append(data[b])
            b += 1

    if a < middle:
        temp += data[a:middle]
    else:
        temp += data[b:right]

    data[left:right] = temp
    return data
