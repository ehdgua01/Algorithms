import itertools


def solution(arr):
    return [n for n, _ in itertools.groupby(arr)]
