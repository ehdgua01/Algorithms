class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = (
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        )
        result = ""
        for roman_num, int_ in symbols:
            if num // int_ != 0:
                s, num = divmod(num, int_)
                result += roman_num * s
        return result
