class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = 0
        
        def backtrack(arr, i, curr):
            nonlocal length
            
            length = max(length, len("".join(curr))) #max_length = 6
            
            for j in range(i, len(arr)):
                val = "".join(curr)
                
                if len(val) + len(arr[j]) == len(set(val + arr[j])):
                    curr.append(arr[j]) ##
                    backtrack(arr, j + 1, curr)
                    curr.pop()
        
        backtrack(arr, 0, [])
        
        return length