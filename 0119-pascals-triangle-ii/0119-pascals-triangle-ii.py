class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]
        
        res = [1,1]
        arr = []
        while rowIndex > 1:
            for i in range(1, len(res)):
                arr.append(res[i] + res[i-1])
            
            res = [1] + arr + [1]
            arr = []
            rowIndex -= 1
        
        return res