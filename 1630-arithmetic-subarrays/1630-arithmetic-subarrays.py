class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            for j in range(1, len(arr)):
                arr[j-1] -= arr[j]
            
            if len(set(arr[0:-1])) == 1:
                l[i] = True
            else:
                l[i] = False
        
        return l
                