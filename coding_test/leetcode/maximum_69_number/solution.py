class Solution:
    def maximum_69_Number(self, num: int) -> str:
        # 짧은 로직: str(num).replace("6", "9", 1)
        # 더 빠른 로직
        num = str(num)
        for i, n in enumerate(num):
            if n == "6":
                num = f"{num[:i]}9{num[i + 1:]}"
                return num
        return num
