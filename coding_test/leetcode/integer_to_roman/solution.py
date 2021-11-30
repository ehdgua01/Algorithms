class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        result = ""
        for int_, roman_num in reversed(symbols.items()):
            if num // int_ != 0:
                result += roman_num * (num // int_)
                num %= int_
        return result
