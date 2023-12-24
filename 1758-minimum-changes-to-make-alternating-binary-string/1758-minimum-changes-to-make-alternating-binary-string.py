class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        prev = s[0]
        for ch in s[1:]:
            if ch == prev:
                count += 1
            prev = str((int(prev) + 1) % 2)
            
        res = count
        count = 1
        prev = str((int(s[0]) + 1) % 2)
        
        for ch in s[1:]:
            if ch == prev:
                count += 1
            prev = str((int(prev) + 1) % 2)
        
        return min(res, count)