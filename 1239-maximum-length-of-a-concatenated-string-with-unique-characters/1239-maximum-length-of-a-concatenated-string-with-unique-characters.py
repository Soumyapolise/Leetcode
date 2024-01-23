class Solution:
    def maxLength(self, arr: List[str]) -> int:
        #res = []
        def backtrack(arr, i, curr):
            nonlocal l
            
            l = max(l, len("".join(curr)))
            
            for j in range(i, len(arr)):
                val = "".join(curr)
                if len(val) + len(arr[j]) == len(set(val + arr[j])):
                    curr.append(arr[j])
                    # res.append(curr[:])
                    
                    backtrack(arr, j+1, curr)
                    curr.pop()
        l = 0            
        backtrack(arr, 0, [])
#         print(res)
        
#         for x in res:
#             l = max(l, len("".join(x)))
            
        return l