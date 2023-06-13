class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        for arr in grid:
            if tuple(arr) in d:
                d[tuple(arr)] += 1
            else:
                d[tuple(arr)] = 1
        count = 0
        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            
            if tuple(temp) in d:
                count += d[tuple(temp)]
        
        return count
        