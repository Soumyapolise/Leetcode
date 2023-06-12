class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        j = 1
        while j<len(nums)+1:
            while j<len(nums) and nums[j] == nums[j-1]+1:
                j+=1
            if (j-i)!=1:
                res += [str(nums[i]) + "->" + str(nums[j-1])]
            else:
                res += [str(nums[j-1])]
            j += 1
            i = j-1
        
        return res