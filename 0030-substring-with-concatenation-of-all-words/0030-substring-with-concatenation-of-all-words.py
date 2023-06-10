class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d_copy = {}
        for word in words:
            if word in d_copy:
                d_copy[word] += 1
            else:
                d_copy[word] = 1
        
        n = len(words[0])
        res = []
        for i in range(len(s)):
            d = d_copy.copy()
            start = i
            while s[i:i+n] in d:
                d[s[i:i+n]] -= 1
                if d[s[i:i+n]] == 0:
                    d.pop(s[i:i+n])
                i += n
            
            if not d:
                res.append(start)
        
        return res