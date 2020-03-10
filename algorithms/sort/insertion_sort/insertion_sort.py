def insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            continue

        swapped = i
        while (
            swapped > 0
            and data[swapped] < data[swapped - 1]
        ):
            data[swapped - 1], data[swapped] = (
                data[swapped], data[swapped - 1]
            )
            swapped -= 1
    return data
