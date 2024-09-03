def solution(n, results):
    wins = [set() for _ in range(n)]
    loses = [set() for _ in range(n)]
    for a, b in results:
        wins[a - 1].add(b - 1)
        loses[b - 1].add(a - 1)
    for i in range(n):
        for loser in wins[i]:
            loses[loser].update(loses[i])
        for winner in loses[i]:
            wins[winner].update(wins[i])
    return sum(
        len(winners) + len(losers) == n - 1 for winners, losers in zip(wins, loses)
    )


def test_cases():
    assert solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]) == 2
    assert (
        solution(
            5,
            [[4, 3], [4, 2], [3, 2], [2, 1], [2, 5], [4, 5], [3, 5], [1, 5]],
        )
        == 5
    )
    assert solution(5, [[2, 3], [2, 4], [2, 5], [1, 2]]) == 2
