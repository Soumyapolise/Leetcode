class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        res = []
        sums = 0
        dirs = [[1, -1], [1, 0], [1, 1]]
        memo = {}
    
        def dfs(i, j, x, y, grid, dirs, memo):
            if i < 0 or i >= len(grid) or x < 0 or x >= len(grid) or j < 0 or j >= len(grid[0]) or y < 0 or y >= len(grid[0]):
                return 0
            
            if (i, j, x, y) in memo:
                return memo[(i, j, x, y)]
            
            if (i, j) != (x, y):
                sums = grid[i][j] + grid[x][y]
            else:
                sums = grid[i][j]
                
            max_cherries = 0
            for di, dj in dirs:
                for dx, dy in dirs:
                    max_cherries = max(max_cherries, dfs(i + di, j + dj, x + dx, y + dy, grid, dirs, memo))
            
            memo[(i, j, x, y)] = sums + max_cherries
            return memo[(i, j, x, y)]
            
        return dfs(0, 0, 0, len(grid[0])-1, grid, dirs, memo)
        
