class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = m*n
        if len(original) != length:
            return []
        
        res = []
        
        for i in range(0, len(original), n):
            res.append(original[i:i+n])
        
        return res
        
        
        