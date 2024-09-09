def solution(k, dungeons):
    result = []
    dfs(k, dungeons, 0, result)
    return max(result, default=0)


def dfs(k, dungeons, n, result):
    available_dungeons = [[m, c] for m, c in dungeons if m <= k]
    if not available_dungeons:
        result.append(n)
        return
    for i, (m, c) in enumerate(available_dungeons):
        dfs(
            k=k - c,
            dungeons=(d for j, d in enumerate(available_dungeons) if j != i),
            n=n + 1,
            result=result,
        )


def test_cases():
    assert solution(80, [[80, 20], [50, 40], [30, 10]]) == 3
