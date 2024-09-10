def solution(name):
    move = sum(get_distance(ord("A"), ord(c), 26) for c in name)
    result = []
    positions = [i for i, c in enumerate(name) if c != "A"]
    dfs(positions, name, 0, move, result)
    return min(result)


def dfs(positions, name, cursor, move, result):
    if not positions:
        result.append(move)
        return

    a, b = positions[0], positions[-1]
    a_pos = get_distance(a, cursor, len(name))
    b_pos = get_distance(b, cursor, len(name))
    dfs(positions[1:], name, a, move + a_pos, result)
    dfs(positions[:-1], name, b, move + b_pos, result)


def get_distance(a, b, length):
    d = abs(a - b)
    return min(d, length - d)


def test_cases():
    assert solution("JEROEN") == 56
    assert solution("JAN") == 23
    assert solution("JAZ") == 11
    assert solution("BBAABABB") == 11
    assert solution("ABAB") == 5
    assert solution("AAABBAAAAZ") == 9
    assert solution("ABBAAABAAAABB") == 15
