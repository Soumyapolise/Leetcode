class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        sums = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = []
                    self.dfs(grid, i, j, res)
                    if res[0] == "#":
                        sums += len(res)
        return sums
    
    def dfs(self, grid, i, j, res):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        
        grid[i][j] = "#"
        res.append("#")
        
        if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
            res[0] = "F"
        
        self.dfs(grid, i + 1, j, res)
        self.dfs(grid, i - 1, j, res)
        self.dfs(grid, i, j + 1, res)
        self.dfs(grid, i, j - 1, res)