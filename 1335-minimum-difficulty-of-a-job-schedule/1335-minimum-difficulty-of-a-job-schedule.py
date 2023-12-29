class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ans = self.findMin(0, d, jobDifficulty, {})
        
        if ans != float('inf'):
            return ans
        else:
            return -1
    
    def findMin(self, index: int, rem: int, nums: List[int], memo: Dict[Tuple[int], int]) -> int:
        
        if index == len(nums) and rem == 0:
            return 0
        
        if index == len(nums) or rem == 0:
            return float('inf')
        
        state = (index, rem)
        if state in memo:
            return memo[state]
        
        maxx = float('-inf')
        minn = float('inf')
        
        for i in range(index, len(nums)):
            maxx = max(maxx, nums[i])
            score = maxx + self.findMin(i+1, rem-1, nums, memo)
            minn = min(minn, score)
        
        memo[state] = minn
        return minn