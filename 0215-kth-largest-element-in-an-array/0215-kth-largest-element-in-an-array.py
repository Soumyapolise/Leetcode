class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        
        left = [x for x in nums if x>pivot] #because we're looking for greatest elements, so decreasing order
        right = [x for x in nums if x<pivot]
        mid = [x for x in nums if x==pivot]
        
        l = len(left)
        r = len(right)
        m = len(mid)
        
        if k <= l:
            return self.findKthLargest(left, k)
        elif k > l+m:
            return self.findKthLargest(right, k-l-m)
        else:
            return mid[0]