def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Required positive number")
    elif n < 2:
        return 1

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result
