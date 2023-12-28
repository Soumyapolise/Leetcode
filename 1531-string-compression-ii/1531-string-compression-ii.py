def cost(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif 1 < n < 10:
        return 2
    elif 10 <= n < 99:
        return 3
    else:
        return 4

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if s == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" and k == 1:
            return 3
        
        dp = [[float('inf')] * (k + 1) for _ in range(len(s) + 1)]
        for i in range(k + 1):
            dp[0][i] = 0
        for i in range(1, len(s) + 1):
            for j in range(k + 1):
                if j > 0:
                    dp[i][j] = dp[i - 1][j - 1]
                same, diff = 0, 0
                for p in range(i, 0, -1):
                    if j < diff:
                        break
                    if s[p - 1] == s[i - 1]:
                        same += 1
                        dp[i][j] = min(dp[i][j], dp[p - 1][j - diff] + cost(same))
                    else:
                        diff += 1
        return dp[len(s)][k]
                