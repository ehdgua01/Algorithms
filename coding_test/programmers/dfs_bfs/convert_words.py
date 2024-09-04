def solution(begin, target, words):
    result = []
    dfs(begin, target, words, 0, result)
    return min(result, default=0)


def dfs(begin, target, words, changes, result):
    if begin == target:
        return True
    for word in words:
        if sum(a != b for a, b in zip(word, begin)) == 1:
            remains = [w for w in words if w != word]
            if dfs(word, target, remains, changes + 1, result):
                result.append(changes + 1)
    return False


def test_cases():
    assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
    assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert solution("aab", "aba", ["abb", "aba"]) == 2
