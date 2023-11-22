class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(val, path, candidates):
            if val == target:
                res.append(path)
                return
            elif val > target:
                return
            
            for i in range(len(candidates)):
                dfs(val + candidates[i], path + [candidates[i]], candidates[i:])
            
        
        dfs(0, [], candidates)
        
        return list(res)
        