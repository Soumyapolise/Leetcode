class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = {}
        cols = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        
        for i in rows.keys(): #1
            matrix[i] = [0]*len(matrix[0])
        
        for i in range(len(matrix)):
            for j in cols.keys(): #1
                matrix[i][j] = 0
            
        
            
        
        
            
                
        