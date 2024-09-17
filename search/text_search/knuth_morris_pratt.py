from typing import Dict, Union


def knuth_morris_pratt(text: str, pattern: str, offset: int = 0) -> Dict[str, Union[str, int]]:
    if offset < 0 or len(text) < offset:
        raise ValueError

    i, j, failure = 0, 1, [0]

    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)

    result = {
        "start": -1,
        "end": -1,
        "match": "",
        "offset": offset,
    }
    i, j = offset, 0

    while i < len(text):
        if pattern[j] == text[i]:
            if len(pattern) == j + 1:
                result["start"] = i + 1 - len(pattern)
                result["end"] = i
                result["match"] = text[result["start"] : result["end"] + 1]
                return result
            j += 1
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return result
