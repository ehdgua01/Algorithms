def solution(routes):
    routes.sort(key=lambda x: x[1])
    k, at = 0, -30_001
    for in_, out in routes:
        if at < in_:
            k += 1
            at = out
    return k


def test_cases():
    assert solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]) == 2
