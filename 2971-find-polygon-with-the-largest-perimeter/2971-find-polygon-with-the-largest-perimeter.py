class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        sums = sum(nums)
        sums -= nums[-1]
        i = 1
        
        while sums > 0:
            if sums > nums[-i]:
                return sums + nums[-i]
            else:
                i += 1
                sums -= nums[-i] 
            
        if sums <= 0:
            return -1
        