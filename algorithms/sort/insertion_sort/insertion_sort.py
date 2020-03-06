def insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            continue

        for j in range(i):
            if data[i] < data[j]:
                data.insert(j, data.pop(i))
                break
    return data
