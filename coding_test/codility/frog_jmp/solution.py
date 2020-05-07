import math


def solution(X: int, Y: int, D: int) -> int:
    return 0 if X == Y else math.ceil((Y - X) / D)
