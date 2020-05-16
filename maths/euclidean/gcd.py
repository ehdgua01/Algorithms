def gcd(n1: int, n2: int) -> int:
    if n1 < n2:
        n1, n2 = n2, n1

    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2

    return n2
