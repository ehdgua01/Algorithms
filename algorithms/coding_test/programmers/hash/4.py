# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려
# 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
#
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열
# plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.


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
        most_plays_genres = ''

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


# 좋은 답안
# def solution(genres, plays):
#     answer = []
#     d = {e: [] for e in set(genres)}
#
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1], e[2]])
#
#     genreSort = sorted(
#         list(d.keys()),
#         key=lambda x: sum(map(lambda y: y[0], d[x])),
#         reverse=True
#     )
#
#     for g in genreSort:
#         temp = [
#             e[1] for e in sorted(
#                 d[g],
#                 key=lambda x: (x[0], -x[1]),
#                 reverse=True
#             )
#         ]
#         answer += temp[:min(len(temp), 2)]
#
#     return answer
