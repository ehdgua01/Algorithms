# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
# 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 내 풀이


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


# 가장 깔끔해 보이는 답안
# import collections
#
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
