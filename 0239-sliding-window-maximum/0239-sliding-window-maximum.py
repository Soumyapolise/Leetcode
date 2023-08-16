from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()

        for i in range(len(nums)):
            while window and window[0] == i-k:
                window.popleft()
            
            while window and nums[window[-1]]< nums[i]:
                window.pop()
            
            window.append(i) #current element
            
            if i>=k-1: #to make sure the 0th and the 1st i won't make the pass ainvayi
                res.append(nums[window[0]])
        
        return res

