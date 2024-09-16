def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = money[1]
    dp1[2] = money[2] + money[0]
    dp2 = [0] * len(money)
    dp2[1] = money[1]
    dp2[2] = money[2]
    for dp in [dp1, dp2]:
        for i in range(3, len(money)):
            dp[i] = money[i] + max(dp[i - 2], dp[i - 3])
    return max(max(dp1[:-1]), max(dp2))


def test_cases():
    assert solution([1, 2, 3]) == 3
    assert solution([3, 2, 1]) == 3
    assert solution([1, 2, 3, 1]) == 4
    assert solution([2, 1, 0, 2]) == 3
    assert solution([1, 0, 1, 0, 0, 1]) == 2
    assert solution([1, 2, 3, 4, 5, 6, 7]) == 15
    assert solution([7, 6, 5, 4, 3, 2, 1]) == 15
    assert solution([7, 7, 5, 7, 3, 7, 1]) == 21
    assert solution([100, 1, 100, 101, 100, 1]) == 300
    assert solution([10, 0, 0, 100, 100, 1_000]) == 1_100
    assert solution([5, 2, 2, 5, 2]) == 10
    assert solution([1_000, 10, 1_000, 10, 10]) == 2_000
    assert solution(list(range(8))) == 16
    assert solution([1_000, 1, 2, 1_000, 4, 5, 1_000, 7]) == 3_000
