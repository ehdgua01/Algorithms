def insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        swapped = i
        while swapped > 0 and data[swapped] < data[swapped - 1]:
            data[swapped - 1], data[swapped] = data[swapped], data[swapped - 1]
            swapped -= 1
    return data
