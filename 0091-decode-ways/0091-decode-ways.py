class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def recursive_decode(idx):
            if idx == len(s):
                return 1
            
            if s[idx] == "0":
                return 0
            
            if idx in memo:
                return memo[idx]
            
            ways = recursive_decode(idx + 1)
            
            if idx + 1 < len(s) and int(s[idx:idx+2]) <= 26: #for two digit numbers
                ways += recursive_decode(idx + 2)
            
            memo[idx] = ways
            
            return ways
        
        return recursive_decode(0)





