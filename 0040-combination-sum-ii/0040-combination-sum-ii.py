class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        d = {}
        self.dfs([], res, target, candidates)
        for key in res:
            if tuple(key) not in d:
                d[tuple(key)] = 1
                
        return list(d.keys())
        
    def dfs(self, arr, res, target, candidates):
        if sum(arr) > target:
            return
        elif sum(arr) == target:
            res.append(arr)
            return
        
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            self.dfs(arr + [candidates[i]], res, target, candidates[i+1:])