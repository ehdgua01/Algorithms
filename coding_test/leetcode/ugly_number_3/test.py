from .solution import Solution


def test_solution():
    nth_ugly_number = Solution().nthUglyNumber
    assert nth_ugly_number(3, 2, 3, 5) == 4
    assert nth_ugly_number(8, 2, 3, 5) == 10
    assert nth_ugly_number(4, 2, 3, 4) == 6
    assert nth_ugly_number(5, 2, 11, 13) == 10
    assert nth_ugly_number(1_000_000_000, 2, 217_983_653, 336_916_467) == 1_999_999_984
