class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return n > 0 and log2(n) == trunc(log2(n))