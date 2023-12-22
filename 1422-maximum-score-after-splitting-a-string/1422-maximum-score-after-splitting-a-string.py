class Solution:
    def maxScore(self, s: str) -> int:
        ones_count = s[1:].count("1")
        if s[0] == "0":
            zeros_count = 1
        else:
            zeros_count = 0
            
        sums = ones_count + zeros_count
        
        for i in range(1, len(s)-1):
            if s[i] == "1":
                ones_count -= 1
            else:
                zeros_count += 1
            
            sums = max(sums, ones_count + zeros_count)
        
        return sums