from itertools import groupby


def solution(A):
    heights = [k for k, _ in groupby(A)]
    if len(heights) < 3:
        return len(heights)
    answer = 2
    for i in range(1, len(heights) - 1):
        prev, curr, next_ = heights[i - 1], heights[i], heights[i + 1]
        if prev < curr > next_ or prev > curr < next_:
            answer += 1
    return answer


def test_solution():
    assert solution([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]) == 4
    assert solution([1, 1, 1, 2, 2]) == 2
    assert solution([-3, -3]) == 1
