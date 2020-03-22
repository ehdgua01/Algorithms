def fibonacci(number: int) -> int:
    if number < 2:
        return number

    a = 0
    b = 1

    for i in range(2, number + 1):
        a, b = b, a + b

    return b
