def solution(number, k):
    stack = []
    for num in number:
        while stack and k and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack[: len(stack) - k])


def test_cases():
    assert solution("1924", 2) == "94"
    assert solution("1924", 3) == "9"
    assert solution("1231234", 3) == "3234"
    assert solution("9199111", 3) == "9991"
    assert solution("4177252841", 4) == "775841"
    assert solution("1111999", 3) == "1999"
    assert solution("00099", 3) == "99"
