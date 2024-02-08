class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        
        def dfs(n):
            nonlocal memo
            
            if n == 0:
                return 0
            
            if n in memo:
                return memo[n]
            
            min_count = float('inf')
            
            for i in range(1, int(n**(0.5)) + 1):
                val = n - i**2
                min_count = min(min_count, dfs(val) + 1)
            
            memo[n] = min_count
            return min_count
        
        dfs(n)
        
        return memo[n]