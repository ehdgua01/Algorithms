"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42579
"""

import itertools
import operator


def solution(genres, plays):
    answer = []
    by_genre = operator.itemgetter(1)
    albums = {
        genre: [id_ for id_, _ in xs]
        for genre, xs in itertools.groupby(
            sorted(enumerate(genres), key=by_genre),
            key=by_genre,
        )
    }
    for genre, _ in sorted(
        albums.items(),
        key=lambda x: sum(plays[id_] for id_ in x[1]),
        reverse=True,
    ):
        answer.extend(sorted(albums[genre], key=lambda x: (-plays[x], x))[:2])
    return answer


def test_cases():
    assert solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    ) == [4, 1, 3, 0]
