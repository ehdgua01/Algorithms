class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return False if x < 10 else x == int(str(x)[::-1])
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_x = 0
        while reversed_x < x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return x == reversed_x or x == reversed_x // 10
