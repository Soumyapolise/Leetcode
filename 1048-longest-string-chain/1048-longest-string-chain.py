class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        
        d = {}
        res = 1
        
        for word in words:
            d[word] = 1
            
            for i in range(len(word)):
                p = word[:i] + word[i+1:]
                
                if p in d:
                    d[word] = max(d[word], d[p] + 1)
                
            res = max(res, d[word])
        
        return res