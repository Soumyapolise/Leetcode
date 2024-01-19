class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        res = float('inf')
        
        def dfs(i, j, memo, matrix):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len(matrix)-1:
                return matrix[i][j]
            
            path1 = dfs(i+1, j-1, memo, matrix)
            path2 = dfs(i+1, j, memo, matrix)
            path3 = dfs(i+1, j+1, memo, matrix)
            
            memo[(i, j)] = matrix[i][j] + min(path1, path2, path3)
            # print(memo)
            return memo[(i, j)]
            
            
        
        for j in range(len(matrix[0])):
            res = min(res, dfs(0, j, memo, matrix))
            
        return res
            