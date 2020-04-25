class Solution:
    def myAtoi(self, str: str) -> int:
        answer = ""

        for s in str.strip():
            if not (s.isdecimal() or (not answer and s in ["-", "+"])):
                break
            answer += s

        try:
            answer = int(answer)
            int32 = 2 ** 31

            if answer < -int32:
                return -int32
            elif int32 - 1 < answer:
                return int32 - 1
            return answer
        except ValueError:
            return 0
