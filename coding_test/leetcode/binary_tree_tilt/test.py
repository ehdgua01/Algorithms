from .solution import Solution, TreeNode


def test_solution():
    solution = Solution().findTilt
    assert (
        solution(
            TreeNode(
                4,
                TreeNode(
                    2,
                    TreeNode(3, None, None),
                    TreeNode(5, None, None),
                ),
                TreeNode(
                    9,
                    None,
                    TreeNode(7, None, None),
                ),
            ),
        )
        == 15
    )
