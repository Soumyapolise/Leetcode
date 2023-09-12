class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        d[0] = 1
        d[1] = 1
        
        def search(n):
            if n in d:
                return d[n]
            
            d[n] = search(n-1) + search(n-2)
        
            return d[n]
        
        return search(n)