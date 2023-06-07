class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 201
        for string in strs:
            length = min(length, len(string)) #min length found
        
        res = ""
        j = 0
        
        while j < length:
            i = 1
            while i<len(strs) and strs[i][j] == strs[0][j]:
                # res += strs[0][j]
                i+=1
            if i == len(strs):
                res += strs[0][j]
            else:
                return res
            j+=1
        
        return res