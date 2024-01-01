class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        prev = "#"
        count = 0
        
        for ch in s:
            #adding the current char into dictionary:
            if ch not in d:
                d[ch] = 0
            if len(ch) >= count:
                d[ch] += 1
                if d[ch] >= 3:
                    count = max(count, len(ch))
                
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
                if len(string) >= count:
                    d[string] += 1
                    if d[string] >= 3:
                        count = max(count, len(string))
        
        
        if count == 0: #did not find anything supporting our clause
            return -1
        
        return count
            
            