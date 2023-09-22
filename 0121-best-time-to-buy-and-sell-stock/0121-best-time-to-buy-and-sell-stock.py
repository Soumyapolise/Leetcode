class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = float('inf')
        res = 0
        
        for p in prices:
            cp = min(cp, p)
            res = max(res, p - cp)
        
        return res