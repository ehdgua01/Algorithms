from collections import Counter
from typing import Counter as CounterType
from typing import List

COINS = [500, 100, 50, 10, 5, 1]


def get_change(price: int, pay: int) -> CounterType[int]:
    assert price < pay

    unit = 0
    change_amount = pay - price
    change: List[int] = []

    while change_amount != 0:
        if 0 < change_amount:
            change_amount -= COINS[unit]
            change.append(COINS[unit])
        else:
            change_amount += change.pop()
            unit += 1

    return Counter(change)
