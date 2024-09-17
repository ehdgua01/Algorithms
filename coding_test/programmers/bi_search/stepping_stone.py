def solution(distance, rocks, n):
    sorted_rocks = sorted((*rocks, distance))
    answer, low, high = 0, 1, distance
    while low <= high:
        mid = (low + high) // 2
        pos = removed = 0
        for rock in sorted_rocks:
            if rock - pos >= mid:
                pos = rock
            else:
                removed += 1
        high, low, answer = (mid - 1, low, answer) if removed > n else (high, mid + 1, mid)
    return answer


def test_cases():
    assert solution(25, [2, 14, 11, 21, 17], 2) == 4
