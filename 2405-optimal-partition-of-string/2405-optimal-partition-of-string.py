class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        substring = ""
        for ch in s:
            if ch in substring:
                count += 1
                substring = ""
            substring += ch
        
        if substring != "":
            count += 1
            
        return count