from .gcd import gcd


def lcm(n1: int, n2: int) -> int:
    __gcd = gcd(n1, n2)
    return (n1 * n2) // __gcd
