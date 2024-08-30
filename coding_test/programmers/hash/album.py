"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42579
"""

from collections import defaultdict


def solution(genres, plays):
    answer = []
    summary = list(zip(genres, plays))
    genres_total_play = defaultdict(lambda: 0)
    genres_include_song = defaultdict(lambda: [])

    for idx, values in enumerate(summary):
        g = values[0]
        gp = values[1]
        genres_total_play[g] += gp
        genres_include_song[g].append(idx)

    while genres_total_play:
        most_plays_count = max(genres_total_play.values())
        most_plays_genres = ""

        for k in genres_total_play.keys():
            if genres_total_play[k] == most_plays_count:
                most_plays_genres = k

        del genres_total_play[most_plays_genres]

        if len(genres_include_song[most_plays_genres]) < 2:
            answer += genres_include_song[most_plays_genres]
            continue

        temp = {}

        for song_index in genres_include_song[most_plays_genres]:
            temp[song_index] = summary[song_index][1]

        for i in range(2):
            song_index = None
            most_plays = max(temp.values())

            for key in temp.keys():
                if most_plays == temp[key]:
                    song_index = key
                    answer.append(song_index)
                    break

            del temp[song_index]

    return answer
