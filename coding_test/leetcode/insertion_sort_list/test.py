from .solution import ListNode, Solution


def test_solution():
    insertion_sort_list = Solution().insertionSortList
    sorted_node = insertion_sort_list(
        ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    )
    current = sorted_node.next
    sorted_values = [sorted_node.val]
    while current:
        sorted_values.append(current.val)
        current = current.next
    assert sorted_values == [1, 2, 3, 4]
