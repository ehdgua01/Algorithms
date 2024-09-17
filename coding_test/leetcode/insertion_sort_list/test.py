from .solution import ListNode, Solution


def test_solution():
    insertion_sort_list = Solution().insertionSortList
    sorted_node = insertion_sort_list(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
    assert list(node.val for node in sorted_node) == [1, 2, 3, 4]
