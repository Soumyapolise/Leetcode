class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        possible = False
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i, i]
            else:
                possible = True
                d[s[i]][1] = i
        
        res = 0

        for val in d.values():
            res = max(res, val[1] - val[0] - 1)
        
        if not possible:
            return -1
        return res