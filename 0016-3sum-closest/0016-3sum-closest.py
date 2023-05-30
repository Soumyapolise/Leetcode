class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = {}
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l<r:
                sums = nums[i] + nums[l] + nums[r]
                if sums<target:
                    res[target-sums] = sums
                    l+=1
                elif sums>target:
                    res[sums-target] = sums
                    r-=1
                else:
                    return sums
                
        mini = min(res.keys())
        return res[mini]