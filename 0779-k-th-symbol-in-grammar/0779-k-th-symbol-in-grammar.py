class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        symbol = 1
        
        for curr_row in range(n, 1, -1):
            total = 2**(curr_row-1)
            half = total//2
            
            if k > half:
                symbol = 1 - symbol
                k -= half
        
        if symbol != 0:
            return 0
        
        return 1