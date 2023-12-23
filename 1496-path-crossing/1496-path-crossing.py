class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        
        i, j = 0, 0
        
        seen.add((i, j))
        d = {"N":[0,1], "E":[1,0], "W":[-1,0], "S":[0,-1]}
        
        for p in path:
            i += d[p][0]
            j += d[p][1]
            
            if (i,j) in seen:
                return True
            
            seen.add((i,j))
        
        return False