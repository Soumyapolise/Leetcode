class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        while matrix!=[]: 
        
            for num in matrix[0]:
                res.append(num)
            if len(matrix)==1:
                matrix = []
            else:
                matrix = matrix[1:]
                n = len(matrix[0])
                for i in range(len(matrix)):
                    for j in range(n//2):
                        matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

                new_mat = [[matrix[j][i] for j in range(len(matrix))] for i in range(n)]
                matrix = new_mat
                        
        return res
            
        
        