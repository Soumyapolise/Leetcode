class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        num = 1
        while k > 0 and num <= n:
            if n%num == 0:
                k -= 1
            num += 1
        
        if num > n and k > 0:
            return -1 
        return num-1