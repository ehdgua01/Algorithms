def anagram(s1: str, s2: str) -> bool:
    s1, s2 = s1.replace(" ", ""), s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    if sorted(s1) != sorted(s2):
        return False

    return True
