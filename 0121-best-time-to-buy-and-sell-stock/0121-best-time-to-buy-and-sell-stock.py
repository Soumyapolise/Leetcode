class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cp = float('inf')
        
        for p in prices:
            cp = min(cp, p)
            
            res = max(res, p - cp)
        
        return res