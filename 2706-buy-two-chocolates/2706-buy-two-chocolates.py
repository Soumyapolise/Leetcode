class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sums = prices[0] + prices[1]
        
        if sums > money:
            return money
        
        return money - sums