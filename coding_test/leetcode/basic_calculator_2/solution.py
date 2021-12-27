from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        nums = deque()
        operator, current = None, 0
        for c in s:
            if c == " ":
                continue
            if c.isdigit():
                current = current * 10 + int(c)
                continue
            self.operate(operator, current, nums)
            operator, current = c, 0
            if len(nums) == 3:  # 메모리 크기 줄이기
                nums.appendleft(nums.popleft() + nums.popleft())

        self.operate(operator, current, nums)
        return sum(nums)

    def operate(self, operator, current, nums):
        if operator is None or operator == "+":
            nums.append(current)
        elif operator == "-":
            nums.append(-current)
        elif operator == "*":
            nums.append(nums.pop() * current)
        else:
            nums.append(int(nums.pop() / current))
