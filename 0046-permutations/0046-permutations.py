class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:]) #[:] creates a copy of the list by slicing - if you append the whole list, and later when you make changes by popping - the changes will be made on all the previous appends of list as well - because they were "copied by reference" - meaning, everything is saved on the same address.
                # print(curr, curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        
        res = []
        backtrack([])
        return res