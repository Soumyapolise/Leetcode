class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        currentStreak, longestStreak = 0, 0
        num_set = set(nums)
        
        for num in nums:
            if num-1 not in num_set:
                currentNum = num
                currentStreak = 1
                
                while currentNum+1 in num_set:
                    currentNum += 1
                    currentStreak += 1
            
                longestStreak = max(longestStreak, currentStreak)
        
        return longestStreak