class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        
        nums.sort()
        
        res = []
        arr = []
        for i in range(n):
            arr.append(nums[i])
            if (i+1)%3 == 0:
                if arr[-1] - arr[0] > k:
                    return []
                res.append(arr)
                arr = []
        
        return res
            