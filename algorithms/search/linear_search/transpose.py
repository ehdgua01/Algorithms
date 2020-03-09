def transpose_linear_search(data: list, match):
    for index in range(len(data)):
        if data[index] == match:
            result = data[index]
            if 0 < index:
                data[index], data[index - 1] = (
                    data[index - 1], data[index]
                )
            return result
