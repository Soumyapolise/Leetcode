class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        
        @cache
        def dp(curr, remain):
            if remain == 0:
                if curr == 0:
                    return 1
            
                return 0
            
            ans = dp(curr, remain-1)
            if curr > 0:
                ans = (ans + dp(curr-1, remain-1)) % mod
            
            if curr < arrLen - 1:
                ans = (ans + dp(curr+1, remain-1)) % mod
            
            return ans
        return dp(0, steps)
        