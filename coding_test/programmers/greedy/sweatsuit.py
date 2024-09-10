def solution(n, lost, reserve):
    lost_set = set(lost).difference(reserve)
    for r in sorted(set(reserve).difference(lost)):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    return n - len(lost_set)


def test_cases():
    assert solution(5, [2, 4], [1, 3, 5]) == 5
    assert solution(5, [2, 4], [3]) == 4
    assert solution(2, [1, 2], [1]) == 1
    assert solution(5, [3, 4], [2, 3]) == 4
    assert solution(3, [3], [1]) == 2
    assert solution(3, [2], [1, 3]) == 3
    assert solution(2, [1], [1]) == 2
    assert solution(3, [1], [1, 2, 3]) == 3
    assert solution(6, [3], [4, 1]) == 6
    assert solution(10, [4, 7, 9], [10, 8]) == 9
    assert solution(10, [4, 7], [1, 6, 8]) == 9
    assert solution(5, [1, 2], [2, 3]) == 4
