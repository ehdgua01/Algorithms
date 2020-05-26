def quick_sort(data: list, left: int, right: int) -> list:
    if right <= left:
        return data

    lesser = index = left
    pivot = data[left]
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

    quick_sort(data, left, lesser - 1)
    quick_sort(data, greater + 1, right)
    return data
