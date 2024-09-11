class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                left, right = s[i + 1 : j + 1], s[i:j]
                return left == left[::-1] or right == right[::-1]
            i += 1
            j -= 1
        return True


def test_valid_palindrome():
    s = Solution()
    assert s.validPalindrome("aba")
    assert s.validPalindrome("a")
    assert s.validPalindrome("aab")
    assert not s.validPalindrome("aabb")
    assert s.validPalindrome("abcba")
    assert s.validPalindrome("abca")
    assert s.validPalindrome("abccbba")
    assert s.validPalindrome("deeee")
    assert not s.validPalindrome("eeccccbebaeeabebccceea")
    assert s.validPalindrome("deddde")
    assert s.validPalindrome(
        "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    )
