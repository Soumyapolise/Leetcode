class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        d = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] in d:
                    for c in d[matrix[i][j]]:
                        if c[0] == i or c[1] == j:
                            return False
                    else:
                        d[matrix[i][j]].append((i,j))
                else:
                    d[matrix[i][j]] = [(i,j)]
        
        return True