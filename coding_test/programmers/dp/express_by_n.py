def solution(n, number):
    answer = -1
    dp = []
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(n) * i))
        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    try:
                        numbers.add(x // y)
                    except ZeroDivisionError:
                        ...
        if number in numbers:
            return i
        dp.append(numbers)
    return answer


def test_solution():
    assert solution(3, 9) == 2
    assert solution(5, 12) == 4
    assert solution(2, 11) == 3
    assert solution(4, 17) == 4
    assert solution(4, 22) == 5
