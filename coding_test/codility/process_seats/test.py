from itertools import groupby


def solution(n: int, s: str):
    total = n * 2
    bc = set("BC")
    hj = set("HJ")
    de = set("DE")
    fg = set("FG")
    for _, seats in groupby(sorted(s.split()), key=lambda x: x[:-1]):
        labels = set(seat[-1] for seat in seats)
        if bc.intersection(labels) and hj.intersection(labels):
            total -= 1
            if de.intersection(labels) or fg.intersection(labels):
                total -= 1
        elif bc.intersection(labels):
            total -= 1
            if fg.intersection(labels):
                total -= 1
        elif hj.intersection(labels):
            total -= 1
            if de.intersection(labels):
                total -= 1
        else:
            if de.intersection(labels):
                total -= 1
            if fg.intersection(labels):
                total -= 1
    return total


def test_solution():
    assert solution(1, "1B 1H") == 1
    assert solution(2, "1A 2F 1C") == 2
    assert solution(1, "") == 2
    assert solution(1, "1D 1F") == 0
    assert solution(1, "1B 1E") == 1
    assert solution(1, "1D 1E") == 1
    assert solution(10, "10D 1D 9H 10G") == 16
    assert solution(1, "1B 1D 1H") == 0
