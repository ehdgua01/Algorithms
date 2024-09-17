import datetime


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    t1 = datetime.datetime(2024, 8, 31, h1, m1, s1)

    if t1.second + t1.minute + t1.hour in [0, 12]:
        answer += 1

    while t1 < datetime.datetime(2024, 8, 31, h2, m2, s2):
        s1_angle = t1.second * 360 / 60
        m1_angle = (t1.minute * 360 / 60) + (t1.second * 360 / 60 / 60)
        h1_angle = (t1.hour % 12 * 360 / 12) + (t1.minute * 360 / 60 / 12) + (t1.second * 360 / 60 / 60 / 12)

        t1 += datetime.timedelta(seconds=1)

        s2_angle = (t1.second * 360 / 60) or 360
        m2_angle = (t1.minute * 360 / 60) + (t1.second * 360 / 60 / 60) or 360
        h2_angle = (t1.hour % 12 * 360 / 12) + (t1.minute * 360 / 60 / 12) + (t1.second * 360 / 60 / 60 / 12) or 360

        if s1_angle < m1_angle and s2_angle >= m2_angle:
            answer += 1

        if s1_angle < h1_angle and s2_angle >= h2_angle:
            answer += 1

        if s2_angle == h2_angle == m2_angle:
            answer -= 1
    return answer
