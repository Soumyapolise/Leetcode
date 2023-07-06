class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=second=float('inf')
        
        for num in nums:
            if num<=first:
                first=num #5
            elif num<=second:
                second=num #12
            else:
                return True
        
        return False