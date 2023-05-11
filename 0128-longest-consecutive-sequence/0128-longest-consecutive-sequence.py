class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        num_set = set(nums)
        i = 0
        while i<len(nums):
            if nums[i]-1 not in num_set:
                currentNum = nums[i]
                currentStreak = 1
                
                while currentNum + 1 in num_set:
                    currentNum += 1
                    currentStreak += 1

                longestStreak = max(longestStreak, currentStreak)
            
            i+=1
        
        return longestStreak