import bisect
from itertools import combinations, product


def solution(dice):
    data = {
        idx_list: sorted(
            sum(dice[v][k] for k, v in zip(x, idx_list))
            for x in product(range(6), repeat=len(idx_list))
        )
        for idx_list in combinations(range(len(dice)), len(dice) // 2)
    }
    result = {}
    for k, v in data.items():
        if k in result:
            continue
        other_key = tuple(i for i in range(len(dice)) if i not in k)
        win = lose = 0
        for x_value in v:
            win += bisect.bisect_left(data[other_key], x_value)
            lose += len(v) - bisect.bisect_right(data[other_key], x_value)
        total = len(v)
        result[k] = win / total * 100
        result[other_key] = lose / total * 100
    answer = sorted(result.items(), key=lambda x: x[1])[-1][0]
    return [i + 1 for i in answer]


def test_cases():
    assert solution(
        [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
    ) == [1, 4]
    assert solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]) == [2]
    assert solution(
        [
            [40, 41, 42, 43, 44, 45],
            [43, 43, 42, 42, 41, 41],
            [1, 1, 80, 80, 80, 80],
            [70, 70, 1, 1, 70, 70],
        ]
    ) == [1, 3]
