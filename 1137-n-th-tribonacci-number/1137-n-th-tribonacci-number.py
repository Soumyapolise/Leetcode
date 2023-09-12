class Solution:
    def tribonacci(self, n: int) -> int:
        d = {}
        
        d[0] = 0
        d[1] = 1
        d[2] = 1
        
        def search(n):
            if n in d:
                return d[n]
            
            d[n] = search(n-1) + search(n-2) + search(n-3)
            return d[n]
    
        return search(n)