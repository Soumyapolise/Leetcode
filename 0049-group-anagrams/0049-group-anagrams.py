class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for string in strs:
            s = "".join(sorted(string))
            if s not in d:
                d[s] = []
            d[s] += [string]
        
        res = []
        
        for val in d.values():
            res += [val]
        
        return res