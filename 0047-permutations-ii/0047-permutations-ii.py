class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, d):
            if len(curr) == len(nums):
                res.append(curr[:])
            
            for n in d:
                if d[n] > 0:
                    # print(n, curr, res, d)
                    curr.append(n)
                    d[n] -= 1
                    backtrack(curr, d)
                    curr.pop()
                    d[n] += 1
        
        res = []
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        backtrack([], d)
        
        return res
        