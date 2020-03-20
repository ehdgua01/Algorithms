def merge_sort(data: list, left: int, right: int):
    if (right - left) < 2:
        return

    a = left
    b = middle = (right + left) // 2
    merge_sort(data, left, middle)
    merge_sort(data, middle, right)

    temp = []

    while a < middle and b < right:
        if data[a] <= data[b]:
            temp.append(data[a])
            a += 1
        else:
            temp.append(data[b])
            b += 1

    if a < middle:
        while a < middle:
            temp.append(data[a])
            a += 1
    else:
        while b < right:
            temp.append(data[b])
            b += 1

    data[left:right] = temp
    return data
