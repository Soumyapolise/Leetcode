class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr):
            if sum(curr) == target:
                if sorted(curr) not in res:
                    res.append(sorted(curr))
                return
            elif sum(curr) > target:
                return
            
            for num in candidates:
                curr.append(num)
                backtrack(curr)
                curr.pop()
        
        res = []
        backtrack([])
        
        return res
        