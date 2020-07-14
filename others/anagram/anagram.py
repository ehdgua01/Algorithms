from collections import Counter


def anagram(s1: str, s2: str) -> bool:
    s1, s2 = s1.replace(" ", ""), s2.replace(" ", "")
    return Counter(s1) == Counter(s2)
