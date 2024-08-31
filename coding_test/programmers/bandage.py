def solution(bandage, health, attacks):
    t, x, y = bandage
    answer = health
    current_time = 0
    for attack_at, damage in attacks:
        casting_time = attack_at - current_time
        answer = min(health, answer + (casting_time * x) + (casting_time // t * y))
        answer -= damage
        if answer < 1:
            return -1
        current_time = attack_at + 1
    return answer
