class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        
        for j in range(len(matrix[0])):
            arr = []
            for i in range(len(matrix)):
                arr.append(matrix[i][j])
            
            res.append(arr)
        
        return res