class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        lis.append(nums[0])
        
        for num in nums[1:]:
            if num > lis[-1]:
                lis.append(num)
            else:
                print(lis)
                for i in range(len(lis)):
                    if lis[i] >= num:
                        lis[i]=num
                        break
        print(lis)
        return len(lis)
                
        