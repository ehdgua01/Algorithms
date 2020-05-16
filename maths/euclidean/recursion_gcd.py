def gcd(n1: int, n2: int) -> int:
    if n1 < n2:
        n1, n2 = n2, n1

    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)
