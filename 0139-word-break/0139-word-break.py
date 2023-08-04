class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # wordDict = set(wordDict)
        
        @lru_cache(None)
        def dfs(start):
            if start == n:
                return True
            
            for end in range(start+1, n+1):
                word = s[start:end]
                if word in wordDict and dfs(end):
                    return True
            
            return False
            
        return dfs(0)
        