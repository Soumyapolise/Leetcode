class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        @cache
        def checker(start):
            if start == n:
                return True
            
            for end in range(start+1, n+1):
                if s[start:end] in wordDict and checker(end):
                    return True
            
            return False
        
        return checker(0)
        