"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42576
"""


def solution(participant, completion):
    answer = ''

    # 한 루프로 처리하고자 참가자와 완주자 목록을 정렬
    participant = sorted(participant)
    completion = sorted(completion)

    for idx, runner in enumerate(participant):
        try:
            if completion[idx] != runner:
                # 정렬한 데이터에서 해당 위치에 존재하지 않음
                answer = runner
                break
        except IndexError:
            # 앞의 모든 참가자들이 완주자일 경우
            answer = runner

    return answer
