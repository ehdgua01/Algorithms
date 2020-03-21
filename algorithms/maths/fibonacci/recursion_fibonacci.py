def recursion_fibonacci(number: int):
    if number == 0:
        return 0
    elif number in [1, 2]:
        return 1

    return recursion_fibonacci(number - 1) + recursion_fibonacci(number - 2)
