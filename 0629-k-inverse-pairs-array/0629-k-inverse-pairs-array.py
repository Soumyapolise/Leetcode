class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1  
        for i in range(2, n + 1):
            v = [0] * (k + 1)
            ps = 0
            for j in range(k + 1):
                ps = (ps + dp[j]) % MOD
                if j >= i:
                    ps = (ps - dp[j - i]) % MOD
                v[j] = ps
            dp = v

        return dp[k]
