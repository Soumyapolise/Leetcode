class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        d = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in d:
                if d[nums[i]] == 1:
                    count += 1
                d[nums[i]] = 1
                d[nums[i] + diff] = 1
            else:
                d[nums[i] + diff] = -1
        
        return count