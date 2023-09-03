class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        return self.dfs(0, 0, memo, m, n)
    
    def dfs(self, i, j, memo, m, n):
        if i == m-1 and j == n-1:
            return 1
        
        if i >= m or j >= n:
            return 0
        
        if memo[i][j] != 0:
            return memo[i][j]
        
        down = self.dfs(i+1, j, memo, m, n)
        right = self.dfs(i, j+1, memo, m, n)
        
        memo[i][j] = down + right
        return memo[i][j]


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         grid = [[0 for _ in range(n)] for _ in range(m)]
#         res = []
#         self.dfs(0, 0, grid, res, m, n)
#         return len(res)
    
#     def dfs(self, i, j, grid, res, m, n):
#         if i < 0 or j < 0 or i >= m or j >= n:
#             return
        
#         if i == m-1 and j == n-1:
#             res.append("#")
#             return
        
#         self.dfs(i+1, j, grid, res, m, n)
#         self.dfs(i, j+1, grid, res, m, n)