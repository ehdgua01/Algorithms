def bubble_sort(data: list) -> list:
    for i in range(len(data) - 1):
        swapped = False

        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                swapped = True
                data[j], data[j + 1] = data[j + 1], data[j]

        if not swapped:
            break
    return data
