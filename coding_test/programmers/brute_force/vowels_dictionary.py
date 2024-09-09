def solution(word):
    d = []
    vowels = ["A", "E", "I", "O", "U"]
    dfs(vowels, "", d)
    return d.index(word) + 1


def dfs(vowels, word, d):
    if len(word) > 4:
        return
    for i, vowel in enumerate(vowels):
        w = f"{word}{vowel}"
        d.append(w)
        dfs(vowels, w, d)


def test_cases():
    assert solution("AAAAE") == 6
    assert solution("AAAE") == 10
    assert solution("I") == 1563
    assert solution("EIO") == 1189
