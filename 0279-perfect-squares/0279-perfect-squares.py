class Solution:
    def numSquares(self, n: int) -> int:
#         memo = {}
        
#         def dfs(n):
#             nonlocal memo
            
#             if n == 0:
#                 return 0
            
#             if n < 0:
#                 return float('inf')
#             if n in memo:
#                 return memo[n]
            
#             min_count = float('inf')
            
#             for i in range(1, int(n**(0.5)) + 1):
#                 val = n - i**2
#                 min_count = min(min_count, dfs(val) + 1)
            
#             memo[n] = min_count
#             return min_count
        
#         dfs(n)
        
#         return memo[n]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Iterate over numbers from 1 to n
        for i in range(1, n + 1):
            # Iterate over perfect squares less than or equal to i
            for j in range(1, int(i**0.5) + 1):
                # Update the minimum count for i
                dp[i] = min(dp[i], dp[i - j**2] + 1)
        
        return dp[n]