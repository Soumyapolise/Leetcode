class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[1,-1], [1,0], [1,1]]
        memo = {}
        
        def dfs(i, j, x, y, grid, dirs, memo):
            nonlocal m
            nonlocal n
            
            if (i, j, x, y) in memo:
                return memo[(i, j, x, y)]
            
            if i < 0 or j < 0 or i >= m or j >= n or x < 0 or y < 0 or x >= m or y >= n:
                return 0
            
            if (i, j) != (x, y):
                sums = grid[i][j] + grid[x][y]
            else:
                sums = grid[i][j]
                
            max_cherries = 0
            for di, dj in dirs:
                for dx, dy in dirs:
                    max_cherries = max(max_cherries, dfs(i+di, j+dj, x+dx, y+dy, grid, dirs, memo))
            
            memo[(i, j, x, y)] = sums + max_cherries
            return memo[(i, j, x, y)]
            
        return dfs(0, 0, 0, n-1, grid, dirs, memo)
        
