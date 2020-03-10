def move_to_front(data: list, target):
    for i in range(len(data)):
        if data[i] == target:
            result = data.pop(i)
            data.insert(0, result)
            return result
