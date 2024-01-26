# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         memo = {}
#         mod = 10**9 + 7
#         def dfs(i, j, memo, num_moves):
#             if i < 0 or j < 0 or i >= m or j >= n:
#                 if num_moves <= maxMove:
#                     if (i,j) in memo:
#                         return memo[(i, j)]%mod
#                     else:
#                         return 1
                
#             if num_moves >= maxMove:
#                 return 0
            
#             memo[(i, j)] = (dfs(i+1, j, memo, num_moves+1)%mod + dfs(i-1, j, memo, num_moves+1)%mod + dfs(i, j+1, memo, num_moves+1)%mod + dfs(i, j-1, memo, num_moves+1)%mod)%mod
            
#             return memo[(i, j)]%mod
        
#         return dfs(startRow, startColumn, memo, 0)

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        mod = 10**9 + 7

        def dfs(i, j, num_moves):
            if num_moves > maxMove:
                return 0

            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

            if (i, j, num_moves) in memo:
                return memo[(i, j, num_moves)] % mod

            result = (dfs(i+1, j, num_moves+1) % mod + dfs(i-1, j, num_moves+1) % mod +
                      dfs(i, j+1, num_moves+1) % mod + dfs(i, j-1, num_moves+1) % mod) % mod

            memo[(i, j, num_moves)] = result
            return result

        return dfs(startRow, startColumn, 0)
