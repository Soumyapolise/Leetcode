class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        res = 0
        i = 0
        
        count = len(piles)//3
        
        while i < len(piles)-count:
            res += piles[i+1]
            i += 2
            
        return res