class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        #dynamic programming solution
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        
        return dp[-1][-1]
        
        
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         if not obstacleGrid:
#             return 0

#         res = [0]  # Using a list to hold the result

#         self.dfs(obstacleGrid, 0, 0, res)
#         return res[0]

#     def dfs(self, grid, i, j, res):
#         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1:
#             return

#         if i == len(grid)-1 and j == len(grid[0])-1:
#             res[0] += 1
#             return

#         grid[i][j] = 1  # Mark the cell as visited to avoid revisiting

#         self.dfs(grid, i+1, j, res) #down
#         self.dfs(grid, i, j+1, res) #right

#         grid[i][j] = 0  # Backtrack: Mark the cell as unvisited
