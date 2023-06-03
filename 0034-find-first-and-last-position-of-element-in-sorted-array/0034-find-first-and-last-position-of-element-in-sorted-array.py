class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        res = [-1,-1]
        while i<=j:
            if nums[i] == target:
                res[0] = i
            
            if nums[j] == target:
                res[1] = j
            
            if res[0] == -1:
                i+=1
            elif res[1] != -1:
                break
                
            if res[1]==-1:
                j-=1
            elif res[0] != -1:
                break
            
            
        return res
            
        
        