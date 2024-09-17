def solution(n, times):
    answer = low = min(times)
    high = max(times) * n
    while low <= high:
        mid = (low + high) // 2
        answer, high, low = (mid, mid - 1, low) if sum(mid // t for t in times) >= n else (answer, high, mid + 1)
    return answer


def test_cases():
    assert solution(6, [7, 10]) == 28
    assert solution(2, [7, 15]) == 14
