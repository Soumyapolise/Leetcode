class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        prev = "#"
        
        for ch in s:
            #adding the current char into dictionary:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
            
            #checking if previous char is equal to the current one and updating prev, if not - updating with current char
            if prev[-1] == ch:
                prev += ch
            else:
                prev = ch
            
            #traversing through "prev" char to update values in dictionary
            for i in range(len(prev)-1):
                string = prev[i:]
                if string not in d:
                    d[string] = 0
                d[string] += 1
        
        res = 0
        for key, val in d.items():
            if val >= 3: #occurring atleast three times
                res = max(res, len(key))
        
        if res == 0: #did not find anything supporting our clause
            return -1
        
        return res
            
            