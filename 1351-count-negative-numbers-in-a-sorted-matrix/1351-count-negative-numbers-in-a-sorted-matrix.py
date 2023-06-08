class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = 0
        j = len(grid[0]) - 1
        count = 0
        while j>=0:
            while i<len(grid):
                if grid[i][j] < 0:
                    count += len(grid)-i
                    break
                i+=1
            j-=1
        
        return count
        
        
        # [4,3,2,-1],
        # [3,2,1,-1],
        # [1,1,-1,-2],
        # [-1,-1,-2,-3]