class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        
        for p in paths:
            if p[1] not in d:
                d[p[1]] = 0
            d[p[1]] += 1
            
            if p[0] not in d:
                d[p[0]] = 0
            d[p[0]] -= 1
        
        for key, val in d.items():
            if val == 1:
                return key