class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def recursive_decode(index):
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index in memo:
                return memo[index]

            ways = recursive_decode(index + 1)

            if index + 1 < len(s) and int(s[index:index + 2]) <= 26:
                ways += recursive_decode(index + 2)

            memo[index] = ways
            return ways

        return recursive_decode(0)





