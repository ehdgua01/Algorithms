"""
프로그래머스 알고리즘 문제

https://programmers.co.kr/learn/courses/30/lessons/42577
"""


def prefix_in_phone(prefix, phone):
    if len(phone) < len(prefix):
        # 번호의 길이가 prefix 길이보다 작으면 안 됨
        return False

    if prefix == phone[: len(prefix)]:
        # 발견
        return True


def solution(phone_book):
    answer = True

    if len(phone_book) == 1:
        # 길이가 하나라면 검사할 필요 없음
        return answer

    for index, prefix in enumerate(phone_book, start=1):
        if index == len(phone_book) - 1:
            # 마지막 번호
            for phone in phone_book[: index - 1]:
                # 자신 뒤의 모든 번호에서 탐색
                if prefix_in_phone(prefix, phone):
                    return False

        else:
            # 시간을 단축해보고자 현재 요소부터 앞 뒤로 탐색함
            for phone in phone_book[index + 1 :]:
                # 자신 앞의 번호 탐색
                if prefix_in_phone(prefix, phone):
                    return False

            for phone in phone_book[: index - 1]:
                # 자신 뒤의 번호 탐색
                if prefix_in_phone(prefix, phone):
                    return False

    return answer
