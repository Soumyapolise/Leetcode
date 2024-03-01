class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(list(s))[::-1]
        return "".join(s[1:]) + "1"