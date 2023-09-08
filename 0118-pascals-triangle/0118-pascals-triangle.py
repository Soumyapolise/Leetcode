class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return res
        
        i = 3
        while i <= numRows:
            lis = []
            for j in range(1, len(res[-1])):
                lis.append(res[-1][j-1] + res[-1][j])
            res.append([1] + lis + [1])
            i += 1
        
        return res
        