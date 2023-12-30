class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        
        for w in words:
            for ch in w:
                if ch not in d:
                    d[ch] = 0
                d[ch] += 1
        
        n = len(words)
        if n == 1:
            return True
        for key, val in d.items():
            if val % n != 0:
                return False
        
        return True