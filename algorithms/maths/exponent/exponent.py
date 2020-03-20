def exponent_func(base: int, exponent: int) -> int:
    if exponent == 1:
        return base
    elif exponent == 0:
        return 1

    if exponent % 2 == 0:
        new_base = exponent_func(base, exponent // 2)
        return new_base * new_base
    else:
        new_base = exponent_func(base, (exponent - 1) // 2)
        return (new_base * new_base) * base
