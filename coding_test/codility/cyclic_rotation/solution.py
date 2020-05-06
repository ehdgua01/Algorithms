from typing import List


def solution(A: List[int], K: int) -> List[int]:
    K = K % len(A) if A and len(A) < K else K
    return A[-K:] + A[0:-K]
