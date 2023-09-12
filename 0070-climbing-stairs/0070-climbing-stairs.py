class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        d[1] = 1
        
        def search(n):
            if n in d:
                return d[n]
            
            if n == 0:
                return 1
            d[n] = search(n-1) + search(n-2)
        
            return d[n]
        
        return search(n)