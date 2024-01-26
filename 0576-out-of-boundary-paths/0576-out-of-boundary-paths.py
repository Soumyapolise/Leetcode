class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        mod = 10**9 + 7

        def dfs(i, j, num_moves):
            if num_moves > maxMove:
                return 0
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            
            if (i, j, num_moves) in memo:  ##storing i, j and num_moves, cuz we wanna keep track of how many moves we CAN make going forward as well. not just the i and j as position.
                return memo[(i, j, num_moves)]%mod
            
            memo[(i, j, num_moves)] = (dfs(i+1, j, num_moves+1)%mod + dfs(i-1, j, num_moves+1)%mod + dfs(i, j+1, num_moves+1)%mod + dfs(i, j-1, num_moves+1)%mod) % mod
            
            return memo[(i, j, num_moves)]

        return dfs(startRow, startColumn, 0)
