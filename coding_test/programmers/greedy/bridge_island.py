def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    tree = [-1] * n
    cost = 0
    for a, b, c in costs:
        while tree[a] != -1:
            a = tree[a]
        while tree[b] != -1:
            b = tree[b]
        if a != b:
            tree[b] = a
            cost += c
    return cost


def test_cases():
    assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
    assert solution(4, [[0, 1, 1], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 7
    assert (
        solution(
            5,
            [
                [0, 1, 5],
                [2, 3, 3],
                [1, 2, 3],
                [3, 1, 2],
                [3, 0, 4],
                [2, 4, 6],
                [4, 0, 7],
            ],
        )
        == 15
    )
