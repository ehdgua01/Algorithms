def solution(sizes):
    sizes = [[max(w, h), min(w, h)] for w, h in sizes]
    return max(w for w, h in sizes) * max(h for w, h in sizes)


def test_cases():
    assert solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4_000
    assert solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120
    assert solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133
