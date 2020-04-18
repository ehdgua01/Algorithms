from typing import List


def solution(operations: List[str]) -> List[int]:
    q = []

    for operation in operations:
        command, val = operation.split()
        val = int(val)

        if command == "I":
            q.append(val)
        elif q:
            if val == -1:
                q.remove(min(q))
            else:
                q.remove(max(q))
    return [max(q), min(q)] if q else [0, 0]
