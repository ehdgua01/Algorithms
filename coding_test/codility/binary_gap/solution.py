import re


def solution(N) -> int:
    return len(max(re.findall(r"(?<=1)0+(?=1)", bin(N)[2:]), default=""))
