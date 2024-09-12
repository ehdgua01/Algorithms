def solution(people, limit):
    people.sort()
    k, left, right = 0, 0, len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        k += 1
    return k


def test_cases():
    assert solution([70, 50, 80, 50], 100) == 3
    assert solution([70, 80, 50], 100) == 3
    assert solution([50, 50], 100) == 1
    assert solution([50, 50, 100], 101) == 2
    assert solution([20, 50, 20, 50, 50, 50], 120) == 3
    assert solution([40], 40) == 1
