class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        res = 0
        
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]  #prefix_sum
        
        for col1 in range(n):
            for col2 in range(col1, n):
                d = {0:1}
                s = 0
                for i in range(m):
                    s += matrix[i][col2]
                    if col1 > 0:
                        s -= matrix[i][col1-1]
                    
                    if s-target in d:
                        res += d[s - target]
                    if s not in d:
                        d[s] = 0
                    d[s] += 1
            
        return res
                
                
        