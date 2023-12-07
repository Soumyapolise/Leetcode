class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        
        while i <= j:
            mid = i + (j-i)//2
            val = 0
            for p in piles:
                val += math.ceil(p/mid)
            
            if val <= h:
                j = mid - 1
            else:
                i = mid + 1
        
        return i