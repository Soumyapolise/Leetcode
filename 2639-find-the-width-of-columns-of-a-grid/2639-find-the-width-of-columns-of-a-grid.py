class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        
        for j in range(len(grid[0])):
            maxi = 0
            for i in range(len(grid)):
                maxi = max(maxi, len(str(grid[i][j])))
            res.append(maxi)
        
        return res