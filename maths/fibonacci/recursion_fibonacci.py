def recursion_fibonacci(number: int) -> int:
    if number < 1:
        return 0
    elif number < 3:
        return 1

    return recursion_fibonacci(number - 1) + recursion_fibonacci(number - 2)
