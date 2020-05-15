def recursion_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Required positive number")

    return 1 if n < 2 else n * recursion_factorial(n - 1)
