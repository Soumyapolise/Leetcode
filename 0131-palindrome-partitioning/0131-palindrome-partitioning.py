class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(s, i, arr, res):
            if i == len(s):
                res.append(arr[:])
                return
            
            for j in range(i, len(s)):
                sub = s[i:j+1]       
                if sub == sub[::-1]:
                    arr.append(sub)
                    backtrack(s, j+1, arr, res)
                    arr.pop()
            
        res = []
        backtrack(s, 0, [], res)
        return res
                          