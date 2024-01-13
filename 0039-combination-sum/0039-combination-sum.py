class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs([], target, res, candidates)
        
        return res
    
    def dfs(self, arr, target, res, candidates):
        if sum(arr) > target:
            return
        
        if sum(arr) == target:
            res.append(arr)
            return
        
        for j in range(len(candidates)):
            self.dfs(arr + [candidates[j]], target, res, candidates[j:])
    
        