from typing import List


def solution(A: List[int]) -> int:
    left_sum, right_sum, answer = 0, sum(A), None
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum -= A[i]
        diff = abs(left_sum - right_sum)
        answer = diff if answer is None else diff if diff < answer else answer
    return answer
