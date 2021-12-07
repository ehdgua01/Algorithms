from .solution import ListNode, Solution


def test_solution():
    solution = Solution().getDecimalValue
    nodes = ListNode(1, ListNode(0, ListNode(1)))
    assert solution(nodes) == 5
    nodes = ListNode(0)
    assert solution(nodes) == 0
    nodes = ListNode(1)
    assert solution(nodes) == 1
    nodes = ListNode(0, ListNode(0))
    assert solution(nodes) == 0
