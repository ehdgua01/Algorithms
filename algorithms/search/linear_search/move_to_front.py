def move_to_front(data: list, match):
    for i in range(len(data)):
        if data[i] == match:
            result = data.pop(i)
            data.insert(0, result)
            return result
