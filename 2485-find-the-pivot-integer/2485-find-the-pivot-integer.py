class Solution:
    def pivotInteger(self, n: int) -> int:
        left = (n * (n+1))//2
        right = n
        n -= 1
        while left != right and n > 0:
            right += n
            left -= n+1
            n -= 1
        # print(n, left)
        if n >= 0 and left == right:
            return n + 1
        
        return -1
        