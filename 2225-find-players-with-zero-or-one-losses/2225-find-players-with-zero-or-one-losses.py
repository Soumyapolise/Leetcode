class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        
        for m in matches:
            if m[0] not in d:
                d[m[0]] = [0,0]
            if m[1] not in d:
                d[m[1]] = [0,0]
            
            d[m[0]][0] += 1
            d[m[1]][1] += 1
            
        res1, res2 = [], []
        
        for key, val in d.items():
            if val[1] == 0:
                res1.append(key)
            
            if val[1] == 1:
                res2.append(key)
        
        return [sorted(res1), sorted(res2)]
            
            
            