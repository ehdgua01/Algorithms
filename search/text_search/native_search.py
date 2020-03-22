from typing import Dict, Union


def native_search(
    text: str, pattern: str, offset: int = 0
) -> Dict[str, Union[str, int]]:
    if offset < 0 or len(text) < offset:
        raise ValueError

    result = {
        "start": -1,
        "end": -1,
        "match": "",
        "offset": offset,
    }

    for i in range(offset, len(text)):
        j = 0
        while j < len(pattern):
            if (len(text) < (j + i)) or (pattern[j] != text[j + i]):
                break

            if len(pattern) == j + 1:
                result["start"] = i
                result["end"] = j + i
                result["match"] = text[i : j + i + 1]
                return result
            j += 1
    return result
