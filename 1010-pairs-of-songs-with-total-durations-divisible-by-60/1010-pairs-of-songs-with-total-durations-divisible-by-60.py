class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        d = Counter(time)
        res = 0
        for t in d:
            if t < 30 :
                res += d[t] * d[60 - t]
        return res + (d[0] * (d[0] - 1) // 2) + (d[30] * (d[30] - 1) // 2)
            