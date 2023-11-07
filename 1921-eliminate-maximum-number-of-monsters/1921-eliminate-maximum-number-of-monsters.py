class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i in range(len(dist)):
            dist[i] = dist[i]/speed[i]
        
        res = 0
        dist.sort()
        i = 0
        time_elapsed = 0
        
        while i < len(dist):
            if dist[i] - time_elapsed > 0:
                res += 1
                time_elapsed += 1 #increasing for every minute the weapon takes to recharge
                i += 1
            else:
                return res
        
        return res
                