class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zCount = 0
        longestWindow = 0
        
        start = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zCount += 1
            else:
                zCount += 0
                
            while zCount > 1:
                if nums[start] == 0:
                    zCount -= 1
                else:
                    zCount -= 0
                    
                start += 1
            
            longestWindow = max(longestWindow, i - start)
        
        return longestWindow