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


"""
사용자의 코드에서 오류가 발생하는 주된 이유는 거리의 최솟값 중 가장 큰 값을 바로 업데이트하는 방식에 있습니다.
문제에서 요구하는 것은 바위를 제거한 후 각 구간 사이의 최솟값 중 최댓값을 찾는 것인데,
여러분의 코드에서는 `min(distances)`를 사용하여 구간 최솟값을 찾고 있지만,
이를 `answer`에 `max(answer, ...)`로 업데이트하는 방식은 문제의 요구사항을 정확하게 충족시키지 못합니다.
코드는 바위 사이의 최소 거리 값이 현재 mid값보다 크거나 같을 때만 거리 배열(`distances`)에 추가하지만,
실제로는 이 최소 거리 값 중 '최대값'을 찾아야 합니다.
이를 위해, 바위를 제거하는 조건과 거리를 계산하는 로직 사이에서 이진 탐색 로직을 정확하게 적용하는 방식을 다시 검토할 필요가 있습니다.
또한, 제거할 바위의 수가 조건을 만족하는 경우 그 때의 중간값(mid)가 바로 답이 될 수 있도록 로직을 조정해야 합니다.
바로 최솟값을 구하는 대신, 제거할 바위의 수가 조건을 만족하면 그 상태에서의 조건을 만족하는 최대의 거리(mid)가 정답이 될 수 있도록 해야 합니다.
"""
