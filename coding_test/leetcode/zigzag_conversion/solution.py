class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = [""] * numRows
        row, direction = 0, True

        for c in s:
            answer[row] += c

            if direction:
                row += 1
            else:
                row -= 1

            if row == 0 or row == numRows - 1:
                direction = not direction
        return "".join(answer)
