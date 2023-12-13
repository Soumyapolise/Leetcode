import numpy
class Solution:
    def numSpecial(self, matrix: List[List[int]]) -> int:
        r = {}
        c = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if (i, 1) not in r:
                        r[(i, 1)] = [0]
                    if (1, j) not in c:
                        c[(1, j)] = [0]
                    
                    r[(i, 1)][0] += 1
                    r[(i, 1)] += [(i, j)]
                    c[(1, j)][0] += 1
                    c[(1, j)] += [(i, j)]
        
        a1, a2 = [], []
        
        for val in r.values():
            if val[0] == 1:
                a1 += val[1:]
        
        for val in c.values():
            if val[0] == 1:
                a2 += val[1:]
        
        count = 0
        for x in a1:
            if x in a2:
                count += 1
        
        return count
                    