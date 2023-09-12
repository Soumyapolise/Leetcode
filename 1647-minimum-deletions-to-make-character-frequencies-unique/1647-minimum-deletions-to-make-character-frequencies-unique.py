class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        
        for ch in s:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        
        lis = sorted(d.values())[::-1]
        res = 0
        print(lis)
        for i in range(1, len(lis)):
            while lis[i] > 0 and lis[i] >= lis[i-1]:
                lis[i] -= 1
                res += 1

        return res
    #4, 1, 1, 1