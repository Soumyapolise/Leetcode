class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        res = [[float('inf') if mat[i][j] == 1 else 0 for j in range(n)] for i in range(m)]

        # Top-left to bottom-right pass
        for i in range(m):
            for j in range(n):
                if i > 0:
                    res[i][j] = min(res[i][j], res[i-1][j] + 1)
                if j > 0:
                    res[i][j] = min(res[i][j], res[i][j-1] + 1)

        # Bottom-right to top-left pass
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    res[i][j] = min(res[i][j], res[i+1][j] + 1)
                if j < n - 1:
                    res[i][j] = min(res[i][j], res[i][j+1] + 1)

        return res


# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         m = len(mat)
#         n = len(mat[0])
#         res = [[0 for _ in range(n)] for _ in range(m)]
        
#         for i in range(m):
#             for j in range(n):
#                 dist = []
#                 if mat[i][j] == 1:
#                     self.dfs(mat, i, j, dist, 0)
#                     res[i][j] = min(dist)
        
#         return res
        
#     def dfs(self, mat, i, j, dist, count):
#         if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or mat[i][j] == -1:
#             return 
        
#         if mat[i][j] == 0:
#             dist.append(count)
#             return
        
#         original_value = mat[i][j]
#         mat[i][j] = -1
        
#         self.dfs(mat, i+1, j, dist, count+1)
#         self.dfs(mat, i-1, j, dist, count+1)
#         self.dfs(mat, i, j+1, dist, count+1)
#         self.dfs(mat, i, j-1, dist, count+1)
        
#         mat[i][j] = original_value