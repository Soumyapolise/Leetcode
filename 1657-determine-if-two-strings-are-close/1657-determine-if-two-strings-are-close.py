class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = {}, {}
        
        for w in word1:
            if w in d1:
                d1[w] += 1
            else:
                d1[w] = 1
        
        for w in word2:
            if w in d2:
                d2[w] += 1
            else:
                d2[w] = 1
                
        return sorted(d1.keys()) == sorted(d2.keys()) and sorted(d1.values()) == sorted(d2.values())