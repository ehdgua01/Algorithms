def bubble_sort(data: list) -> list:
    for i in range(len(data) - 1):
        for j in range(len(data) - (i + 1)):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data
