def binary_search(data: list, size: int, target):
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
