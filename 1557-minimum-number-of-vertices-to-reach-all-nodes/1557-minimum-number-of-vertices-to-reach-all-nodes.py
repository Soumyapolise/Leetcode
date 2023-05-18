class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = {}
        
        for e in edges:
            d[e[1]] = 1
        
        res = []
        
        for x in range(n):
            if x not in d:
                res.append(x)
        
        return res