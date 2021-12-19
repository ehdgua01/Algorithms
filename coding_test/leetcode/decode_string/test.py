from .solution import Solution


def test_solution():
    decode_string = Solution().decodeString
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc3[cd]xyz") == "abccdcdcdxyz"
    assert decode_string("100[leetcode]") == "leetcode" * 100
    assert (
        decode_string("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
        == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    )
