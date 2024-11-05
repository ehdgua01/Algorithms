from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [
            f"{h}:{m:02}" for h in range(12) for m in range(60) if bin(h).count("1") + bin(m).count("1") == turnedOn
        ]


def test_binary_watch():
    s = Solution()
    assert s.readBinaryWatch(1) == ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]
    assert s.readBinaryWatch(9) == []
