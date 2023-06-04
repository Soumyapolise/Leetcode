class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        for i in range(len(s)):
            count = 0
            seen = set()
            while i<len(s) and s[i] not in seen:
                seen.add(s[i])
                i+=1
                count += 1
            maxi = max(maxi, count)
        
        return maxi
            