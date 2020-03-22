from typing import Dict, Union


def boyer_moore(text: str, pattern: str, offset: int = 0) -> Dict[str, Union[str, int]]:
    if offset < 0 or len(text) < offset:
        raise ValueError

    result = {
        "start": -1,
        "end": -1,
        "match": "",
        "offset": offset,
    }

    i = offset

    while i < (len(text) - len(pattern) + 1):
        mismatch_index, match_index = -1, -1

        for p in range(len(pattern) - 1, -1, -1):
            if pattern[p] != text[i + p]:
                mismatch_index = i + p
                break

        if mismatch_index == -1:
            result["start"] = i
            result["end"] = i + len(pattern) - 1
            result["match"] = text[result["start"] : result["end"] + 1]
            return result
        else:
            for j in range(len(pattern) - 1, -1, -1):
                if text[mismatch_index] == pattern[j]:
                    match_index = j
            i = mismatch_index - match_index
    return result
