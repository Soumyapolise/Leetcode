class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while(n > 0):
            print(n)
            n -= 1
            curr = n % 26
            n = n//26
            res += chr(curr + ord('A'))
        
        return res[::-1]