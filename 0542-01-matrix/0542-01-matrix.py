from collections import deque
class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        # Enqueue all cells with value 0 and mark them as visited
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1  # Mark non-zero cells as visited

        distance = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if 0 <= newRow < m and 0 <= newCol < n and mat[newRow][newCol] == -1:
                        mat[newRow][newCol] = distance
                        queue.append((newRow, newCol))

            distance += 1

        return mat



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
        
#         mat[i][j] = -1