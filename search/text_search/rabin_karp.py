from typing import Dict, Union


def hashing(plaintext: str) -> int:
    hash_value = 0
    for i, t in enumerate(plaintext, start=1):
        hash_value += ord(t) * (2 ** (len(plaintext) - i))
    return hash_value


def rabin_karp(text: str, pattern: str, offset: int = 0) -> Dict[str, Union[str, int]]:
    if offset < 0 or len(text) < offset:
        raise ValueError

    result = {
        "start": -1,
        "end": -1,
        "match": "",
        "offset": offset,
    }

    hash_value = None
    hash_pattern = hashing(pattern)

    for i in range(offset, len(text)):
        if len(text) < (i + len(pattern)):
            return result

        if hash_value is None:
            hash_value = hashing(text[i : i + len(pattern)])
        else:
            hash_value = 2 * (
                hash_value - (ord(text[i - 1]) * (2 ** (len(pattern) - 1)))
            ) + ord(text[i + len(pattern) - 1])

        if hash_value == hash_pattern:
            result["start"] = i
            result["end"] = i + len(pattern) - 1
            result["match"] = text[result["start"] : result["end"] + 1]
            return result
    return result
