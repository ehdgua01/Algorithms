from collections import Counter


def solution(nums):
    return len(Counter(nums).most_common(len(nums) // 2))
