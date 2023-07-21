class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        
        for i in range(n): #4
            for j in range(i): #3
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1 # [1,2,3,3,4]
                        count[i] = 0 #[1,0,0,0,0]
                    if length[j] + 1 == length[i]: #[1,1,1,1,1]
                        count[i] += count[j] #[1,0,0,0,0]
        
        max_length = max(length) #2
        result = 0
        
        for i in range(n):
            if length[i] == max_length:
                result += count[i]
        
        return result