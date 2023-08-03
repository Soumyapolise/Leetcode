class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr):
            # print(curr, res)
            if sum(curr) == target:
                if sorted(curr) not in res:
                    res.append(sorted(curr)[:])
                return 
            elif sum(curr) > target:
                return 
            
            for n in candidates:
                curr.append(n)
                backtrack(curr)
                curr.pop()
        
        res = []
        backtrack([])
        return res
        