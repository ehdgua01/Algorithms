class Solution:
    def intToRoman(self, num: int) -> str:
        keys = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        result = ""
        for roman_num, int_ in zip(keys, values):
            if num // int_ != 0:
                s, num = divmod(num, int_)
                result += roman_num * s
        return result
