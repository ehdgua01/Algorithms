import random


def check_dup(r: int) -> bool:
    if r < 1:
        raise ValueError()

    range_ = range(1, r + 1)

    if 0 < len(set(range_).difference(random.choices(range_, k=r))):
        return True

    return False
