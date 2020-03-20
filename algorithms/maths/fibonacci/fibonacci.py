def fibonacci(number: int):
    if number <= 1:
        return number

    a = 0
    b = 1

    for i in range(2, number + 1):
        a, b = b, a + b

    return b
