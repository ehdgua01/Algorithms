def transpose_linear_search(data: list, target):
    for index in range(len(data)):
        if data[index] == target:
            result = data[index]
            if 0 < index:
                data[index], data[index - 1] = (
                    data[index - 1], data[index]
                )
            return result
