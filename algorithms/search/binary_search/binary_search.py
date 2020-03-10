def binary_search(data: list, size: int, match):
    left = 0
    right = size - 1

    while left <= right:
        pivot = round((left + right) / 2)
        if data[pivot] == match:
            return data[pivot]
        elif data[pivot] < match:
            left = pivot + 1
        else:
            right = pivot - 1
