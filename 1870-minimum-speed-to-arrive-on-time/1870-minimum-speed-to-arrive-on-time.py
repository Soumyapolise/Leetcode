import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        r = 1e7+1
        
        while l<r:
            mid = l + (r-l)//2
            res = 0
            for d in dist[0:len(dist)-1]:
                res += (d+mid-1)//mid
            
            res += dist[-1]/mid
            
            if res > hour:
                l = mid + 1
            else:
                r = mid
        
        if l == 1e7+1:
            return -1
        else:
            return int(l)
    
                
            
        
        