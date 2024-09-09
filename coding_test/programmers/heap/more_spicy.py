import heapq


def solution(scoville, K):
    scoville.sort()
    mixed = 0
    while len(scoville) > 1 and scoville[0] < K:
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)
        s = first + second * 2
        heapq.heappush(scoville, s)
        mixed += 1
    return mixed if scoville[0] >= K else -1


def test_cases():
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2
    assert solution([1], 2) == -1
    assert solution([2], 2) == 0
    assert solution([2, 3], 2) == 0
