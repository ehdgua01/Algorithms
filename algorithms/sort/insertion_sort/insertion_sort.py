def insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            continue

        value = data[i]
        for j in range(i):
            if value < data[j]:
                data.insert(j, data.pop(i))
                break
    return data
