class Solution:
    def totalMoney(self, n: int) -> int:
#         1, 2, 3, 4, 5, 6, 7 - 28
#         2, 3, 4, 5, 6, 7, 8 - 35
#         3, 4, 5, 6, 7, 8, 9 - 42
        
        
        if n <= 7:
            return (n*(n+1))//2
        
        val = n//7
        rem = (n % 7)
        res = 0
        
        for k in range(1, val+1):
            res += (k + 3)*7
        for x in range(1, rem+1):
            res += val + x
        
        return res