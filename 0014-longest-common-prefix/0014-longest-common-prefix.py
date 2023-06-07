class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        res = ""
        
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                res += first[i]
            else:
                return res
        return res
        
        
#         length = 201
#         for string in strs:
#             length = min(length, len(string)) #min length found
        
#         res = ""
#         j = 0
        
#         while j < length:
#             i = 1
#             while i<len(strs) and strs[i][j] == strs[0][j]:
#                 i+=1
#             if i == len(strs):
#                 res += strs[0][j]
#             else:
#                 return res
#             j+=1
        
#         return res