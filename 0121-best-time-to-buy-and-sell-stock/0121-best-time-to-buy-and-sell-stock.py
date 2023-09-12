class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = float('inf')
        profit = 0
        
        for p in prices:
            cp = min(cp, p)
            profit = max(profit, p - cp)
            
        return profit
                
            