class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(candidates, target, res, path)
        return res
    
    def dfs(self, candidates, target, res, path):
        print(candidates, path)
        if target < 0:
            return
        
        if target == 0:
            res.append(path)
            return
        
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target-candidates[i], res, path + [candidates[i]])
        
#         def backtrack(curr):
#             if sum(curr) == target:
#                 if sorted(curr) not in res:
#                     res.append(sorted(curr)[:])
#                 return
#             elif sum(curr) > target:
#                 return
            
#             for num in candidates:
#                 curr.append(num)
#                 backtrack(curr)
#                 curr.pop()
        
#         res = []
#         backtrack([])
        
#         return res
        