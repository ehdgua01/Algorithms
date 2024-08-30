"""
퀵 정렬의 최악의 경우를 피하는 방법 중 하나
정렬 작업 전에 배열의 인덱스를 랜덤으로 섞어 주는 전처리 작업을 추가해서 최악의 경우를 피한다.
"""

import random
from typing import Any, List

from .quick_sort import quick_sort


def shuffle_quick_sort(data: List[Any]) -> List[Any]:
    random.shuffle(data)
    return quick_sort(data, 0, len(data) - 1)
