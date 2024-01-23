class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = []
        
        def backtrack(arr, res, i, curr):
            if i == len(arr):
                res.append(curr[:])
                return
            
            for j in range(i, len(arr)):
                val = "".join(curr)
                if len(val) + len(arr[j]) == len(set(val + arr[j])):
                    curr.append(arr[j])
                    res.append(curr[:])
                    
                    backtrack(arr, res, j+1, curr)
                    curr.pop()
        l = 0            
        backtrack(arr, res, 0, [])
        for x in res:
            l = max(l, len("".join(x)))
            
        return l