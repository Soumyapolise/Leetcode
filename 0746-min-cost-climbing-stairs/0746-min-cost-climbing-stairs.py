class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        sums = 0
        def dfs(i, cost):
            if i >= len(cost):
                return 0
            
            if i in d:
                return d[i]
            
            val = cost[i] + min(dfs(i+1, cost), dfs(i+2, cost))
            
            d[i] = val
            return d[i]
           
        return min(dfs(0, cost), dfs(1, cost))