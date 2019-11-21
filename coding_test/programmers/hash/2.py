# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
#
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.


# 내 풀이

def prefix_in_phone(prefix, phone):
    if len(phone) < len(prefix):
        # 번호의 길이가 prefix 길이보다 작으면 안 됨
        return False

    if prefix == phone[:len(prefix)]:
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
            for phone in phone_book[:index - 1]:
                # 자신 뒤의 모든 번호에서 탐색
                if prefix_in_phone(prefix, phone):
                    return False

        else:
            # 시간을 단축해보고자 현재 요소부터 앞 뒤로 탐색함
            for phone in phone_book[index + 1:]:
                # 자신 앞의 번호 탐색
                if prefix_in_phone(prefix, phone):
                    return False

            for phone in phone_book[:index - 1]:
                # 자신 뒤의 번호 탐색
                if prefix_in_phone(prefix, phone):
                    return False

    return answer


# 제일 깔끔해 보이는 답안
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
